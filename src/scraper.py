import os
import time
import random
import threading
import pandas as pd
import csv
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Number of worker threads, max by default
n_workers = os.cpu_count()

SCRIPT_DIR = Path(__file__).parent.resolve()
OUTPUT_DIR = SCRIPT_DIR / "chat_results"
EXCEL_PATH = SCRIPT_DIR / "Group C.xlsx"
CSV_COUNTS_PATH = SCRIPT_DIR / "message_counts.csv"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_driver_chrome():
    ua = UserAgent()
    opts = ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument(f"user-agent={ua.random}")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    # service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(options=opts)

def create_driver_firefox():
    ua = UserAgent()
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    opts.set_preference("general.useragent.override", ua.random)
    opts.set_preference("dom.webdriver.enabled", False)
    opts.set_preference("useAutomationExtension", False)
    # service = Service(GeckoDriverManager().install())
    return webdriver.Firefox(options=opts)

def scrape_chat(url, driver):
    """Returns list of (role, text) tuples"""
    if not isinstance(url, str) or not url.startswith("http"):
        print(f"Invalid URL: {url}")
        return None
    try:
        driver.get(url)
        time.sleep(random.uniform(2, 5))
        soup = BeautifulSoup(driver.page_source, "html.parser")

        msgs = []
        for article in soup.find_all("article"):
            if article.find("p"):
                text = "\n".join(p.get_text(strip=True) for p in article.find_all("p"))
                msgs.append(("AGENT", text))
            else:
                text = article.get_text(strip=True, separator="\n")
                if text.startswith("You said:"):
                    text = text.replace("You said:", "").strip()
                    msgs.append(("USER", text))
        return msgs
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Function executed by each worker 
def process_task(task):
    response_id, threat_type, threat_num, url, writer, write_lock, pbar = task
    # You will probably want to change this to create_driver_chrome()
    driver = create_driver_firefox()
    try:
        messages = scrape_chat(url, driver)
        if not messages:
            return
        
        # Write chat to .txt
        filename = OUTPUT_DIR / f"{response_id}-{threat_type}-{threat_num}.txt"
        with write_lock:
            with open(filename, "w", encoding="utf-8") as f:
                for i, (role, text) in enumerate(messages, 1):
                    f.write(f"{role} {i}:\n{text}\n\n")

        # Count and write to CSV
        prompts = sum(1 for r, _ in messages if r == "USER")
        responses = sum(1 for r, _ in messages if r == "AGENT")
        with write_lock:
            writer.writerow([response_id, threat_type, threat_num, prompts, responses, url])
    except Exception as e:
        print(f"Error processing {url}: {e}")
    finally:
        driver.quit()
        # Update progress bar
        with write_lock:
            pbar.update(1)

def main():
    df = pd.read_excel(EXCEL_PATH, sheet_name="Sheet0")
    # Build list of tasks
    tasks = []
    for _, row in df.iterrows():
        response_id = row["ResponseId"]
        for prefix, threat_type in [("Q85", "GitHub"), ("Q86", "Kubernetes")]:
            for col in (c for c in row.index if c.startswith(prefix) and c.endswith("_2")):
                url = row[col]
                if pd.notna(url):
                    threat_num = col.split("_")[1]
                    tasks.append((response_id, threat_type, threat_num, url))

    write_lock = threading.Lock()
    with open(CSV_COUNTS_PATH, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ResponseID", "ThreatType", "ThreatNumber", "Prompts", "Responses", "URL"])

        with tqdm(total=len(tasks), desc="Processing URLs", unit="url") as pbar:
            worker_args = [(response_id, threat_type, threat_num, url, writer, write_lock, pbar) for response_id, threat_type, threat_num, url in tasks]
            # Dispatch
            with ThreadPoolExecutor(max_workers=n_workers) as exe:
                futures = [exe.submit(process_task, args) for args in worker_args]
                for _ in as_completed(futures):
                    pass

    # Sort the CSV file
    data = pd.read_csv(CSV_COUNTS_PATH)
    data.sort_values(by=["ResponseID", "ThreatType", "ThreatNumber"], inplace=True, ignore_index=True)
    data.to_csv(CSV_COUNTS_PATH, index=False)

    print(f"Results saved to {CSV_COUNTS_PATH}")

if __name__ == "__main__":
    main()
