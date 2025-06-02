# The role of Data Flow Diagrams in validating identified security threats- Replication package
This repository contains the data used to execute a control experiement to measure the role of a data flow diagram in validating security threats. The experiement was conducted in two universities, in the Netherlands and China.

### How to Cite us
To be updated....
The scientific article describing design, execution, and main results of this study is available here.
If this study is helping your research, consider to cite it is as follows, thanks!

@article{mbaka2025validating,

  title={Assessing the usefulness of Data Flow Diagrams for validating security threats},
  
  author={Mbaka, Winnie Bahati and Zhang, Xinran and Wang, Yunduo and Li, Tong and Massacci, Fabio and Tuma, katja},
  
  journal={Computers & Security},
  
  volume={},
  
  pages={},
  
  year={2025},
  
  publisher={}
}

### General overview
Several steps were followed in it's execution. 
First we prepared all textual materials. This included choosing relevant but comparable scenarios. To this end, we presented a kubernetes and a GitHub scenario for the first and confirming experiments. To further make the student's background knowledge comparable , for the subjects relevant to this study (security and the domains of the selected scenarios), we developed training videos.
From the scenarios, we compiled 10 threats, each containing a unique thretad ID, threat description, assumption, affected components, and an associated STRIDE threat type. 5 of the threats were real and 5 were fabricated.
Additional reading materials, selcted book chapters on STRIDE were also made availabe.

To measure the role of the data flow diagram in validating threats, we proposed comparing it to a process diagram, a sequence diagram. To this end, we defined two treatment group. Intervention received both the DFD and sequence diagram while control group received only a sequence diagram.

### The Task
From the list of threats, the participants were required to identify/choose the actual threats.


### Available material for replication
To aide in the replication, we have made available the following materials;
1. Scenario descriptions, with a sequence diagram and a data flow diagram
2. List of threats, one from the Kubernetes scenario and one from the GitHub scenario
3. Sample entry questionnaire
4. Sample participants report and exit questionnaire
5. python notebook




### Getting started
To execute the python file:
1. First dowload the "sample participants report and exit questionnaire" file. The format of the csv file is the same as the one used during this data analysis.
2. Add the csv file to your Google drive
3. Open the .ipynb file and follow the specified steps. 
4. Change the drive directory and the file name of the downloaded csv sheet 
5. All relevant python packages have already been pre-defined where necessary



## Repository Structure
This is the root directory of the repository. The directory is structured as follows:

    template-replication-package
     .
     |--- data/                            Contains sample data obtained from participants reports. All identifiable information has been removed.
     |
     |--- documentation/                   Contains the scenario description for each experiement, the list of threats adopted from each scenario and a document containing the justification for the validity of each threat alongside the information cues and technical knowledge necessary for validating the threats.
     |
     |--- src/                             Contains the python notebook with a step-by-step analysis of the data obtained from participants. We did not provide the actual data used in analysis, however, the data format follows the same columns contained in the excel files uploaded in the "Data folder" in this repository. 
    
    
     
                         
  



