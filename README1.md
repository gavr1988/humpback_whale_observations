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

- Winter observations area ssociated with the highest mean SST at approximately 24.36C, whilst summer observations had a much lower SST of approximately 14.43 oC. This should not be interpreted as meaning the whole north pacific is warmer in Winter, as the pattern may partially reflect differences in where whales were recorded during each session.

 A T-test comparing Winter and Summer SST produced a t-statistic of approximately 286.23 and a p-value displayed by Python as 0.0. The p-value is effectively zero and below the 0.05 significance level, so the null hypothesis was rejected.

- The correlation between SST and SSS was approximately 0.56, indicating a moderate positive relationship between the two environmental variables within the observation data.

- Of the three machine-learning models tested, the unrestricted Decision Tree produced the lowest testing RMSE at approximately 0.05°C. However, it also fitted the training data almost perfectly, so its ability to generalise to genuinely new years or geographical areas should be treated cautiously.

Overall, the results show clear seasonal and environmental differences within the recorded observations. However, these patterns represent associations within the available data and should not be interpreted as direct evidence of whale abundance or causation.

## Streamlit Application. 

As part of this projected I created a multipage interactive Streamlit application, which is used to present and display the main findings of the project in a user friendly accesible format. 

The application contains five main pages. 

1. **Home/Overview**

This page provides an introduction to the project, including the research question and a summary of the main findings. 

2. **SST and Seasonal Analysis**

This page allows the user to explore recorded observations and sea surface temperature patterns using season and year filters. 

3. **Observation Maps**

This page displays the geographical locations of recorded humpback whale observations. 
It can be filtered by season and year to allow the user to compare. 

4. **SST Predictitions**

THis page uses the trained decision tree regression model to estimate sea-surface temperature from year, month, latitude and longitude. 

5. **Methodology and Limitations**

This explains the data-cleaning process, statistical analysis , machine learning, project limitations, ethical considerations and use of AI.

The reason this streamlit was designed and created was designed to make the results easier to explore and visualise without requiring the user to run through the entire jupyter notebook or even understanding the python coding. 

## Challenges and Solutions

I came across several practical challenges during the development of this project. 

### 1. A Large Dataset

Challenge : The original dataset from OBIS was approximately 333.1 MB, which made it too large to upload to the GitHub repository associated with this project. 

Solution : In order to deal with this the orignal dataset was stored locally and added to the `.gitignore`. A smaller cleaned dataset was created and used for the analysis and creation of the streamlit.  

### 2. Missing and Incorrect Month Values

Challenge: Some records contained missing or unreliable values in the month column.

Solution: To address this, the observation date was converted into a datetime format and the month was extracted from the date where possible. This allowed the season variable to be created more reliably.

### 3. Updating Results after Filtering

Challenge : During development, the dataset was filtered to include only records between 2010 and 2025. This changed some of the statistical results that had been calculated earlier in the project.

Solution: The analysis was rerun and the written interpretations were checked and updated so that they matched the latest outputs.

### 4. Machine-Learning Development

Challenge: Errors were encountered while preparing and training the regression models, particularly when dealing with missing values and selecting suitable input variables.

Solution: The data was checked before modelling, records with missing values required by the model were removed, and the models were evaluated using RMSE so that their performance could be compared.

### 5. File Paths and Project Organisation

Challenge: As the project structure developed, some file paths stopped working because files and folders had been reorganised.

Solution: The working directory was checked and file paths were updated so that the Jupyter Notebook and Streamlit application could locate the required datasets correctly.




