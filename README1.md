# North Pacific Humpback Whale Observation Analysis

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