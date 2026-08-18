# North Pacific Humpback Whale Observation Analysis

## Repository

[GitHub Repository](https://github.com/gavr1988/humpback_whale_observations)

## Project Overview

This capstone project investigates recorded North Pacific humpback whale observations and explores how these observations vary by season and sea-surface temperature between 2010 and 2025.

## Research Question

How do North Pacific humpback whale observations vary by season and
sea-surface temperature between 2010 and 2025?

## Project Objectives

- Clean and prepare the OBIS dataset. 
- Explore seasonal observation patterns. 
- Analyse SST and SSS. 
- Apply statistical testing. 
- Build an interactive Streamlit dashboard to host the findings and allow for exploration. 

## Dataset

The dataset was obtained from the Ocean Biodiversity Information System (OBIS).

The data can be accessed from the OBIS Mapper:

https://mapper.obis.org/?taxonid=137092&areaid=31908&startdate=2010-01-01#

The dataset used for this project was downloaded on 24 July 2026.


## Data Management

The original dataset was downloaded from the Ocean Biodiversity Information System (OBIS) on 24 July 2026.

The data was originally downloaded as a Tab-Separated Values (TSV) file. I converted this into a CSV file using Apple Numbers.

It was then saved locally as:

`whale_data_original.csv`

Because of the size of this dataset (331.1 MB), it has not been uploaded to the GitHub repository and has been added to the `.gitignore` file.

After the data was cleaned and filtered in the Jupyter Notebook, the processed data was saved as:

`whale_data_cleaned.csv`

The cleaned dataset contains 118,209 recorded observations.

During data cleaning, missing SST and SSS values were not estimated or replaced. Records with missing environmental measurements were excluded only from analysis steps that required those variables.

Git and GitHub were used for version control so that changes to the project files, code and documentation could be tracked throughout the development of the project.


## Project Structure

The project has been organised into separate folders for the Jupyter Notebook, Streamlit application and visualisations.


## Project Structure

The project has been organised into separate folders for the Jupyter Notebook, Streamlit application and visualisations.

```text
humpback_whale_observations/
│
├── figures/
│   └── Contains visualisations created during the analysis.
│
├── jupyter_notebooks/
│   └── Contains the main Jupyter Notebook used for data cleaning,
│       statistical analysis and machine learning.
│
├── streamlit/
│   ├── app.py
│   ├── whale_data_cleaned.csv
│   └── pages/
│       ├── 1_sst_seasonal_analysis.py
│       ├── 2_observation_map.py
│       ├── 3_sst_prediction.py
│       └── 4_methodology_and_limitations.py
│
├── .gitignore
├── README.md
├── requirements.txt
├── Procfile
├── setup.sh
└── visualisations.py
```

### Main Files and Folders

- `jupyter_notebooks/` contains the main Jupyter Notebook used for data cleaning, exploratory analysis, statistical testing and machine learning as well as the graphical representation of the analysis. 

- `streamlit/` contains the interactive Streamlit application.

- `streamlit/app.py` is the main homepage for the Streamlit dashboard.

- `streamlit/pages/` contains the additional pages for seasonal analysis, the observation map, SST prediction, and methodology and limitations.

- `whale_data_cleaned.csv` contains the cleaned dataset used by the Streamlit application.

- `figures/` contains visualisations created in the Jupyter Notebook during the project.

- `requirements.txt` lists the Python packages required to run the project.

- `Procfile` and `setup.sh` are used for deployment.

- `.gitignore` prevents files such as the large original dataset (`whale_data_originial`) from being tracked by Git such as the original data downloaded from OBIS.

- `README.md` contains the main documentation for the project.

## Methodology

The Project followed an exploratory data analysis to investigate seasonal patterns in recorded humpback whale observations in the North Pacific region whilst also looking into the sea-surface temperature associated with the observations.

The main stages of the project were:

1. The original OBIS dataset was cleaned and filtered using pandas. 
2. The relevant variables such as date, month, latitude, longitude, SST and SSS were then selected. 
3. The data was filtered to only display records between 2010 and 2025. 
4. A season variable was then created from the observation month. 
5. Descriptive statistics were calculated for SST and SSS. 
6. Seasonal observation patterns were explored using visualisations and basic probability. 
7. A T-Test was then used to compare winter and Summer mean SST (this was decided on from the analysis).
8. Correlation analysis was used to investigate the relationship between SST and SSS.
9. A series of regression models were created using Scikit-learn to find the best model to predict SST from year, month, latitude and longitude.
10. The main findings were presented through an interactive Streamlit application. 

## Key Findings

The analysis identified several seasonal and environmental patterns within the recorded humpback whale observations. 

- Winter contained the largest number of recorded observations with 38,034 records. 
- Winter observations area ssociated with the highest mean SST at approximately 24.36C, whilst summer observa