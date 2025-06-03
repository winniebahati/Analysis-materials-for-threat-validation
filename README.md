# Less is more: Usefulness of data flow diagrams and large language models for security threat validation
This repository contains the data used to execute a control experiement to measure the role of a data flow diagram and large language models in validating security threats. We first conducted a pilot with 41 MSc students and a think aloud with three practitioners. The outcomes of the think-aloud were analysed for potential issues and concerns that needed to be addressed before the final data collection campaign. The final data collection was done via Upword, a crowdsourcing platform, where 68 expert practitioners were hired to participate in the experiement.

### How to Cite us
To be updated....
The scientific article describing design, execution, and main results of this study is available here.
If this study is helping your research, consider to cite it is as follows, thanks!

@article{xyz.....,

  title={Less is more: Usefulness of data flow diagrams and large language models for security threat validation},
  
  author={Mbaka, Winnie Bahati and Tuma, katja},
  
  journal={Empirical Software Engineering},
  
  volume={},
  
  pages={},
  
  year={2025},
  
  publisher={}
}

### General overview
Several steps were followed in it's execution. 
First we prepared all textual materials. This included choosing relevant but comparable scenarios. To this end, we presented a kubernetes and a GitHub scenario for the first and confirming experiments. To further make the student's background knowledge comparable , for the subjects relevant to this study (security and the domains of the selected scenarios), we developed training videos.
From the scenarios, we compiled 10 threats, each containing a unique thretad ID, threat description, assumption, affected components, and an associated STRIDE threat type. 5 of the threats were real and 5 were fabricated.
Additional reading materials, on Data Flow Diagrams were also made availabe.

To measure the role of the data flow diagram and large language models in validating threats, we make use of a balanced orthogonal design which is also known as Taguchi Design. Each participant
is randomly assigned to one of the four groups:

1) LLM + DFD (A) receives the scenario descriptions with an accompanying data flow diagram instance and tasked with assessing the applicability of threats using an LLM
2) noLLM + DFD (B) receives the scenario descriptions with an accompanying data flow diagram instance and tasked with self-assessing the applicability of threats
3) LLM + noDFD (C) receives the scenario description without an accompanying data flow diagram instance and tasked with assessing the applicability of threats using an LLM
4) noLLM + noDFD (D) receives the scenario description without an accompanying data flow diagram instance and tasked with self-assessing the applicability of threats

### The Task
From the list of threats, the participants were required to identify/choose the actual threats.


### Available material for replication
To aide in the replication, we have made available the following materials;
1. Scenario descriptions, with a sequence diagram and a data flow diagram
2. List of threats, one from the Kubernetes scenario and one from the GitHub scenario
3. Python notebook


### How to get started
We only provide teh anonymised participants ressponses to the questionnaires upon request.
The accompanying Python script contains the code used to address our research questions, with all required packages already specified.

# Web Scraper Tool

This project includes a Python script for scraping chatGPT conversation between the LLM and participants and a `requirements.txt` file specifying all necessary Python packages.

## Project Contents

- `scraper.py`: The main Python script for web scraping.
- `requirements.txt`: Lists all dependencies required to run the script.

## 🛠️ Installation

Before running the script, make sure you have **Python 3.7+** installed on your system.

1. Clone the repository or download the files

2. Install the required packages:

        pip install -r requirements.txt

3. Run the scraping script using:
   
        python scraper.py




## Repository Structure
This is the root directory of the repository. The directory is structured as follows:

    template-replication-package
     .
     |--- data/                            Contains pre-screening questions for recruiting experts from Upwork and 
     |
     |--- Materials/                       Contains the scenario descriptions, the ground truth, information cues and knowledge required to validate each threat,         transcription codes for the analysis of the think-aloud interviews, the surveys for each tratment group, STride training and the pre-screening questionnaires.
     |
     |--- src/                             Contains the python notebook with a step-by-step analysis of the data obtained from participants, the script used to scrape the chat conversations between participants and ChatGPT. We provide the actual data used in analysis upon request. 
    
    
     
                         
  



