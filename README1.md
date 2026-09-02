# North Pacific Humpback Whale Observation Analysis

## Repository

[GitHub Repository](https://github.com/gavr1988/humpback_whale_observations)

## Project Overview

This capstone project investigates recorded North Pacific humpback whale observations and explores how these observations vary by season and sea-surface temperature between 2010 and 2025.

## Research Question

How do North Pacific humpback whale observations vary by season and
sea-surface temperature between 2010 and 2025?

## Hypothesis

Before carrying out the analysis, I hypothesised that the number of recorded humpback whale observations would be higher during the Summer months.

This hypothesis was influenced by information from the International Whaling Commission (IWC) Whale Watching Handbook, which explains that Northern Hemisphere humpback whale populations migrate seasonally and generally feed at higher latitudes between June and October.

As my project focuses on the North Pacific, I expected this seasonal movement towards northern feeding grounds to result in a greater number of recorded observations during the Summer months.

However, observation records can also be influenced by factors such as survey effort, tourism, accessibility and reporting practices, so the number of recorded observations should not be interpreted as a direct measure of humpback whale abundance.

## Project Objectives

- Clean and prepare the OBIS dataset. 
- Explore seasonal observation patterns. 
- Analyse SST and SSS. 
- Apply statistical testing. 
- Build an interactive Streamlit dashboard to host the findings and allow for exploration. 

## Target Audience

The target audience for this project includes people with an interest in marine ecology, wildlife conservation, environmental data and humpback whales, as well as users who may not have a technical background in data analytics.

The Jupyter Notebook provides the more detailed technical analysis, including data cleaning, statistical testing, correlation analysis and machine-learning development for those with a data analytics background. 

The Streamlit application was designed to make the main findings easier to understand for a wider audience. It allows users to explore the data using filters, summary statistics, visualisations, an observation map and an SST prediction tool without needing to understand or run the underlying Python code.

To support non-technical users, the dashboard also includes explanations of the methodology, limitations and interpretation of the results. Care was taken to describe the data as recorded whale observations rather than direct measures of whale abundance.

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

- `.gitignore` prevents files such as the large original dataset (`whale_data_original`) from being tracked by Git such as the original data downloaded from OBIS.

- `README.md` contains the main documentation for the project.

## Project Plan

An original project plan was created to outline the intended stages of the project, including data collection, cleaning, exploratory analysis, statistical testing, machine learning, visualisation and project documentation. The original plan can be found in the file `project_plan.md`

The project plan was adapted during development as new challenges, findings and learning opportunities emerged.

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

- Winter observations were associated with the highest mean SST at approximately 24.36°C, whilst Summer observations had a lower mean SST of approximately 14.43°C. This should not be interpreted as meaning that the whole North Pacific is warmer in Winter, as the pattern may partly reflect differences in where whales were recorded during each season.

 A T-test comparing Winter and Summer SST produced a t-statistic of approximately 286.23 and a p-value displayed by Python as 0.0. The p-value is effectively zero and below the 0.05 significance level, so the null hypothesis was rejected.

- The correlation between SST and SSS was approximately 0.56, indicating a moderate positive relationship between the two environmental variables within the observation data.

- Of the three machine-learning models tested, the unrestricted Decision Tree produced the lowest testing RMSE at approximately 0.05°C. However, it also fitted the training data almost perfectly, so its ability to generalise to genuinely new years or geographical areas should be treated cautiously.

Overall, the results show clear seasonal and environmental differences within the recorded observations. However, these patterns represent associations within the available data and should not be interpreted as direct evidence of whale abundance or causation.

The initial hypothesis was also not supported by the recorded observation data, as Winter contained the highest number of records rather than Summer.

## Streamlit Application. 

As part of this I created a multipage interactive Streamlit application, which is used to present and display the main findings of the project in a user friendly accessible format. 

The application contains five main pages. 

1. **Home/Overview**

This page provides an introduction to the project, including the research question and a summary of the main findings. 

2. **SST and Seasonal Analysis**

This page allows the user to explore recorded observations and sea surface temperature patterns using season and year filters. 

3. **Observation Maps**

This page displays the geographical locations of recorded humpback whale observations. 
It can be filtered by season and year to allow the user to compare. 

4. **SST Predictions**

This page uses the trained decision tree regression model to estimate sea-surface temperature from year, month, latitude and longitude. 

5. **Methodology and Limitations**

This explains the data-cleaning process, statistical analysis , machine learning, project limitations, ethical considerations and use of AI.

The reason this streamlit was designed and created was designed to make the results easier to explore and visualise without requiring the user to run through the entire jupyter notebook or even understanding the python coding. 

## Challenges and Solutions

I came across several practical challenges during the development of this project. 

### 1. A Large Dataset

Challenge : The original dataset from OBIS was approximately 331.1 MB, which made it too large to upload to the GitHub repository associated with this project. 

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


### 6. Learning Streamlit

Challenge: I had limited previous experience using Streamlit before this project, so developing a multipage application presented an additional learning challenge.  


Solution: I utilised AI to assist in the development of the application and did so gradually, starting with the homepage and then adding separate pages for seasonal analysis, the observation map, SST prediction, and methodology and limitations. Each page was tested as it was developed. The original plan for the Streamlit app can be found in .`streamlit_dashboard_plan.md`.

### 7. Naming Conventions

Challenges: During the project I received feedback that the naming conventions used for files and folders could be improved alongside my commit titles for github. 

Solution: The repository was reorganised to use clearer and more consistent lowercase `snake_case` naming for Python files and folders. This improved the readability and organisation of the project. I also gave more detailed commits after receiving this feedback.


## Limitations

There are several limitations that should be considered when interpreting the findings of this project.

- The dataset contains recorded humpback whale observations rather than a complete measure of the humpback whale population. A higher number of records does not necessarily mean that more whales were present, as observation numbers may also be influenced by survey effort, tourism, accessibility and reporting practices.

- The dataset does not contain reliable information about locations where whales were searched for but not observed. Because of this, the project cannot be used to calculate the true probability of whale presence or absence.

- Some records were missing SST and SSS values. These values were not estimated, and records with missing measurements were excluded only from analyses that required those variables.

- Geographical location may influence the seasonal SST patterns. For example, the higher mean SST associated with Winter observations should not be interpreted as meaning that the whole North Pacific is warmer in Winter.

- The hypothesis test used very large sample sizes. With large datasets, even relatively small differences can produce very small p-values, so the statistical results were considered alongside descriptive statistics and visualisations.

- The machine-learning models were evaluated using a random training and testing split. Similar geographical or temporal records may therefore have appeared in both datasets, which could make model performance appear better than it would on completely new years or geographical areas.

- The relationships identified between season, SST, SSS and recorded observations represent associations within the dataset and should not be interpreted as evidence of causation.

## Ethics and Data Governance

The project uses environmental and wildlife observation data obtained from the Ocean Biodiversity Information System (OBIS). The dataset does not contain personal information such as names, addresses or contact details.

However, ethical considerations are still important when working with biodiversity data. The dataset includes geographical coordinates showing where humpback whales have been recorded, so wildlife-location information should be handled responsibly. In this project, the coordinates are used to investigate broad geographical patterns rather than to encourage the location of individual animals.

Care was also taken when interpreting and presenting the results. Observation counts are described as recorded observations rather than direct measures of whale abundance, because differences in survey effort, accessibility, tourism and reporting practices may influence the number of records.

The same approach was taken with the environmental analysis. Relationships between season, SST, SSS and recorded observations are described as associations and are not presented as proof that one variable directly causes changes in whale distribution.

The original OBIS data source is acknowledged throughout the project. The original dataset is stored separately from the cleaned dataset so that the cleaning and analysis process can be checked and reproduced.

AI assistance was also used during the project. AI-generated suggestions were treated as guidance rather than automatically assumed to be correct, and code, statistical results and interpretations were checked against the actual outputs from the dataset before being included in the final project.

## Use of AI

AI, specifically ChatGPT, was used as a support tool during several stages of this project.

It was used to help with:

- Identifying the relevant variables within the original OBIS dataset to use in my analysis.
- Troubleshooting Python errors during data cleaning and analysis throughout the project completion.
- Understanding statistical concepts and terminology such as hypothesis testing, p-values and Root Mean Squared Error (RMSE).
- Troubleshooting issues encountered while developing the machine-learning models.
- Supporting the interpretation of statistical and machine-learning outputs.
- Learning how to structure and develop the multipage Streamlit application.
- Improving project organisation and documentation.

AI-generated suggestions were not automatically assumed to be correct. Code was run and tested in the Jupyter Notebook and Streamlit application, and statistical results and interpretations were checked against the actual outputs from the dataset.

During the project, I found that AI tools can sometimes provide incorrect code, make assumptions or confidently present inaccurate information. For this reason, AI was used as a learning and troubleshooting tool rather than as a replacement for checking the analysis myself.

The responsibility for the final code, analysis, interpretation and conclusions remained with me.

## Future Development and Maintenance

Although the current project answers the main research question, there are several ways it could be developed further.

### Data Updates

The OBIS database may continue to receive new humpback whale observation records. Future versions of the project could download updated data and repeat the existing cleaning process to include more recent observations.

When the source data is updated, the cleaned dataset would also need to be regenerated so that the Jupyter Notebook and Streamlit application continue to use the latest available information.

### Machine-Learning Model

If the dataset is updated, the machine-learning models would need to be retrained and evaluated using the new data.

A future improvement would be to evaluate the model using observations from different years or geographical regions rather than relying only on a random train/test split. This would provide a stronger test of how well the model performs on genuinely new data.

Additional environmental variables could also be investigated to determine whether they improve SST prediction.

### Further Analysis

Future analysis could investigate the geographical distribution of recorded humpback whale observations in greater detail.

This could include examining how observation locations change between seasons and years and investigating whether geographical patterns help explain the differences in SST associated with the recorded observations.

### Streamlit Application

The Streamlit application could be expanded as further analysis is completed. Additional visualisations, filters or environmental variables could be added to allow users to explore the dataset in more detail.

The application should also be tested after any changes to the dataset, model or Python dependencies to ensure that all pages continue to work correctly.

### Project Maintenance

The Python packages listed in `requirements.txt` should be reviewed periodically and updated when required.

Any updates to the project should be tested locally before being committed to GitHub and deployed to the live application.

Git and GitHub can continue to be used to track changes and provide a record of how the project develops over time.


## How to Run the Project

To run this project locally follow these steps:

1. Clone the GitHub repository using `git clone https://github.com/gavr1988/humpback_whale_observations.git`

2. Move into the project folder using `cd humpback_whale_observations`

3. Create a virtual environment using `python3 -m venv .venv`

4. Activate the virtual environment on macOS/Linux using `source .venv/bin/activate`

5. Install the required Python packages using `pip install -r requirements.txt`

6. Open the Jupyter Notebook using `jupyter notebook jupyter_notebooks/capstone_humpback_whales.ipynb`

7. To run the Streamlit application locally, use `streamlit run streamlit/app.py`

The original OBIS dataset, `whale_data_original.csv`, is approximately 331.1 MB and is not included in the GitHub repository because of its size. The original data can be downloaded from the OBIS Mapper linked in the Dataset section of this README.

The cleaned dataset required by the Streamlit application is included in the repository.

The deployed Streamlit application can also be accessed here:

[Humpback Whale Analytics](https://humpback-sst-analysis-4af99d9204ef.herokuapp.com/)

## Reflection and Learning

This project allowed me to develop my skills in Python, data analysis, statistics, machine learning and data visualisation while working with a large real-world dataset surrounding a topic that interests me.

The original OBIS dataset contained a large number of variables, missing values and some issues with dates and months. Working through these problems helped me understand how important it is to check the quality and structure of data before relying on the results for analytical purposes.

I also developed my understanding of descriptive statistics, probability, hypothesis testing and correlation. Rather than only calculating the results, I learned to consider what the results actually mean and the limitations of the conclusions that can be made from them.

The machine-learning section gave me experience using Scikit-learn to create, train and compare regression models. I learned how Root Mean Squared Error (RMSE) can be used to compare prediction error and also learned that a model performing very well on a test dataset does not automatically mean that it will perform equally well on completely new data.

Developing the Streamlit application was another important part of the project for me. I had very little experience with Streamlit, and it gave me the opportunity to turn the Jupyter Notebook analysis into an interactive application that can be used by somebody without needing to understand or run the underlying Python code. Whilst I utilised AI to support the creation of the Streamlit application, I feel I was still able to demonstrate my own ideas and will continue to practise using Streamlit in other projects I take on.

Throughout the project I encountered problems involving missing data, file paths, machine-learning models, project organisation and deployment preparation. Solving these problems helped improve my confidence in troubleshooting code and breaking larger problems into smaller steps.

I also learned the importance of reviewing results as a project changes. For example, after filtering the dataset to the final 2010–2025 period, some earlier statistical results and written interpretations needed to be updated. This showed me why code, outputs and documentation need to remain consistent with each other.

Overall, the project has improved my confidence in working independently with a real-world dataset and has given me a better understanding of the full data analysis process, from obtaining and cleaning data through to analysis, machine learning, visualisation and presenting the final results.

## Testing

Testing was carried out throughout the development of the project to make sure the Jupyter Notebook and Streamlit application worked as expected.

### Jupyter Notebook Testing

The Jupyter Notebook was tested by running the analysis from beginning to end and checking that:

- The dataset loaded correctly.
- The cleaning steps produced the expected columns and data types.
- The data was filtered to observations between 2010 and 2025.
- The season variable was created correctly.
- Summary statistics and visualisations produced the expected outputs.
- The hypothesis test and correlation analysis ran successfully.
- The machine-learning models trained successfully and produced RMSE values for comparison.

### Streamlit Testing

The Streamlit application was tested locally and after deployment.

Testing included:

- Checking that all five application pages loaded successfully.
- Testing the season and year filters.
- Checking that summary statistics changed when filters were applied.
- Checking that the seasonal charts displayed correctly.
- Testing the observation map.
- Testing the SST prediction tool using different inputs.
- Checking that the cleaned dataset loaded correctly on each page.
- Checking that the application displayed correctly after deployment to Heroku.

### Deployment Testing

After deployment to Heroku, the live application was tested to confirm that:

- The application started successfully.
- All Streamlit pages were accessible.
- The cleaned dataset loaded correctly.
- Interactive filters and visualisations worked.
- The SST prediction tool returned a result.
- No file-path or missing-package errors prevented the application from running.




## Deployment

The Streamlit application has been deployed using Heroku.

The live application can be accessed here:

[Humpback Whale Analytics](https://humpback-sst-analysis-4af99d9204ef.herokuapp.com/)

The deployment files included in the repository are:

- `Procfile`
- `setup.sh`
- `requirements.txt`

These files provide Heroku with the information required to install the project dependencies and run the Streamlit application.

## References and Acknowledgements

The following data sources, articles and documentation were used during the development of this project.

### Data Source

- **Ocean Biodiversity Information System (OBIS)**  
  Humpback whale occurrence data used for this project.  
  [OBIS Mapper](https://mapper.obis.org/?taxonid=137092&areaid=31908&startdate=2010-01-01#)

  The dataset used in this project was downloaded on 24 July 2026.

### Marine Ecology and Data Analytics

- **Plymouth Marine Laboratory (PML)**  
  *Big Data to Protect Marine Biodiversity*  
  [Plymouth Marine Laboratory](https://pml.ac.uk/portfolio/big-data-to-protect-marine-biodiversity/)

- **Frontiers in Marine Science**  
  *Data Science and Artificial Intelligence for Advancing Marine Science and Technology*  
  [Frontiers in Marine Science](https://www.frontiersin.org/research-topics/75955/data-science-and-artificial-intelligence-for-advancing-marine-science-and-technology)

- **Harnham**  
  *How Data is Playing a Role in Preserving Marine Ecosystems*  
  [Harnham](https://www.harnham.com/how-data-is-playing-a-role-in-preserving-marine-ecosystems-harnham-recruitment-post/)

- **Unity Environmental University**  
  *Data and the Deep Sea: Ways Marine Biologists Use Data and Scientific Analysis to Save the Oceans*  
  [Unity Environmental University](https://unity.edu/sustainability/data-and-the-deep-sea-4-ways-marine-biologists-use-data-and-scientific-analysis-to-save-the-oceans/)

  ### Humpback Whale Ecology

- **International Whaling Commission (IWC) – Whale Watching Handbook**  
  Information about humpback whale migration, feeding and seasonal distribution was used to help inform the initial project hypothesis.  
  [Humpback Whale – Whale Watching Handbook](https://wwhandbook.iwc.int/en/species/humpback-whale)

### Technical Documentation

- **Scikit-learn**  
  Scikit-learn documentation was used to support the development and troubleshooting of the regression models used in this project.  
  [Linear Regression Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

  - **Streamlit**  
  Streamlit documentation was used to support the development of the interactive application, including the geographical observation map.  
  [Streamlit `st.map` Documentation](https://docs.streamlit.io/develop/api-reference/charts/st.map)

### Acknowledgements

AI assistance, specifically ChatGPT, was used as a learning and troubleshooting tool during the development of this project. Further details about how AI was used and how its outputs were checked are provided in the **Use of AI** section above.


 