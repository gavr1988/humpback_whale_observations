# Project Plan

In this file I include the original plan for my project:

## Project Title

North Pacific Humpback Whale Observation Analysis

## Research Question

How do North Pacific humpback whale observations vary by season and sea-surface temperature between 2010 and 2025?

## Initial Project Aim

The aim of this project was to use a real-world marine biodiversity dataset to investigate seasonal patterns in recorded humpback whale observations and explore the environmental conditions associated with those observations.

## Initial Objectives

- Obtain humpback whale observation data from OBIS.
- Convert the observation data obtained from OBIS from a tsv file to a csv file
- Clean and prepare the dataset using Python and Pandas.
- Investigate seasonal observation patterns.
- Analyse Sea-Surface Temperature (SST) and Sea-Surface Salinity (SSS).
- Use descriptive statistics and visualisations to explore the data.
- Apply statistical testing to investigate differences within the dataset.
- Explore the use of machine learning within the analysis.
- Create an interactive dashboard to communicate the findings.
- Use Git and GitHub to manage and document the project.

## Initial Project Stages

### 1. Data Collection

Obtain humpback whale observation data from the Ocean Biodiversity Information System (OBIS).

### 2. Data Cleaning

Use Python and Pandas to:

- Select relevant variables.
- Check missing values.
- Correct date and month information.
- Filter the required years.
- Create seasonal categories.
- Prepare SST and SSS data for analysis.

### 3. Exploratory Data Analysis

Use descriptive statistics and visualisations to investigate:

- Recorded observations by season.
- SST distributions.
- Seasonal SST differences.
- SSS distributions.
- Relationships between SST and SSS.
- Changes across the 2010–2025 analysis period.

### 4. Statistical Analysis

Use appropriate statistical methods to investigate patterns identified during exploratory analysis.

This included descriptive statistics, basic probability, correlation analysis and hypothesis testing.

### 5. Machine Learning

Explore whether regression models could be used to predict Sea-Surface Temperature from temporal and geographical variables.

Compare model performance using Root Mean Squared Error (RMSE).

### 6. Data Visualisation and Communication

Create visualisations within the Jupyter Notebook and develop an interactive dashboard using tableau to allow users to explore the main findings.

### 7. Documentation and Version Control

Use Git and GitHub throughout the project to track changes.

Document the project methodology, findings, limitations and instructions within the README.

## Expected Outputs

The planned outputs of the project were:

- A completed Jupyter Notebook containing the analysis.
- A cleaned dataset.
- Statistical analysis and visualisations.
- Machine-learning model comparison.
- An interactive dashboard.
- A documented GitHub repository.
- A README explaining the project and findings.

## Changes to the Original Plan

The project developed and changed as the analysis progressed.

One significant change was the decision to use Streamlit instead of tableau as the main interactive dashboard. I initially had limited experience with Streamlit, so this became an additional learning opportunity during the project.

The dataset was also filtered to the final analysis period of 2010–2025 during development. This required some earlier results and written interpretations to be recalculated and updated.

The machine-learning stage also developed through experimentation. Three regression models were compared, and their performance and limitations were evaluated using training and testing RMSE.

The project structure, naming conventions, and regular commitment names were also improved following feedback received during development.

These changes demonstrate how the original project plan was adapted in response to the data, technical challenges, feedback and learning throughout the project.