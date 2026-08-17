import streamlit as st


#Page Configuration

st.set_page_config(
    page_title="Methodology & Limitations",
    page_icon="📋",
    layout="wide"
)


#Page Title and Introduction

st.title("Methodology & Limitations")

st.write(
    "This page explains how the humpback whale observation data "
    "was prepared and analysed, together with the main limitations, "
    "ethical considerations and use of AI during the project."
)


#About the Dataset

with st.expander("About the Dataset"):

    st.write(
        """
        This project uses humpback whale observation data obtained from the
        Ocean Biodiversity Information System (OBIS).

        The analysis focuses on recorded North Pacific humpback whale
        observations between 2010 and 2025 and investigates how these
        observations vary by season and the sea-surface temperatures
        associated with them.

        The cleaned dataset contains 118,209 recorded observations.
        Of these, 114,308 records contain Sea-Surface Temperature (SST)
        data and 114,308 contain Sea-Surface Salinity (SSS) data.

        The dataset also contains temporal and geographical information
        including observation date, month, latitude and longitude.
        """
    )


# Data Cleaning and Preparation

with st.expander("Data Cleaning"):

    st.write(
        """
        The original OBIS dataset contained a large number of variables,
        so I selected the columns that were most relevant to the research
        question.

        These included observation date, year, month, latitude, longitude,
        Sea-Surface Temperature (SST), Sea-Surface Salinity (SSS) and
        information relating to the observation records.

        Pandas was used to prepare and clean the dataset.
        """
    )

    st.markdown(
        """
        The cleaning process included:

        - Selecting the relevant columns from the original dataset.
        - Converting columns to appropriate data types.
        - Identifying missing values.
        - Checking and converting observation dates.
        - Filtering the dataset to observations between 2010 and 2025.
        - Correcting the month column using the observation date.
        - Creating a season variable from the month.
        - Checking latitude and longitude values.
        - Creating separate datasets for SST and SSS analysis.
        - Saving the cleaned dataset as a CSV file.
        """
    )

    st.write(
        """
        Records with missing SST or SSS values were excluded only from
        analyses that required those variables. I chose not to estimate
        environmental values that were not present in the original data.
        """
    )


#Statistical Analysis

with st.expander("Statistical Analysis"):

    st.write(
        """
        Several statistical methods were used to investigate the
        environmental conditions associated with the recorded humpback
        whale observations.
        """
    )

    st.markdown(
        """
        The analysis included:

        - Mean
        - Median
        - Standard deviation
        - Minimum and maximum values
        - Percentiles
        - Interquartile Range (IQR)
        - Basic probability
        - Welch's independent t-test
        - Correlation analysis
        """
    )

    st.write(
        """
        Basic probability was used to calculate the proportion of recorded
        observations belonging to each season. Winter contained the largest
        proportion at approximately 34.28%, while Spring contained the
        smallest proportion at approximately 20.73%.
        """
    )

    st.write(
        """
        A Welch's independent t-test was used to compare the mean SST
        associated with Winter and Summer observations. The test did not
        assume that the two groups had equal variances.

        The test found a statistically significant difference between
        Winter and Summer mean SST.
        """
    )

    st.write(
        """
        Correlation analysis was also used to investigate the relationship
        between SST and SSS. The correlation coefficient was approximately
        0.56, indicating a moderate positive relationship within the
        observation data.
        """
    )


# Machine Learning

with st.expander("Machine Learning"):

    st.write(
        """
        Scikit-learn was used to investigate whether Sea-Surface Temperature
        could be predicted using temporal and geographical information.

        The predictor variables were:
        """
    )

    st.markdown(
        """
        - Year
        - Month
        - Latitude
        - Longitude
        """
    )

    st.write(
        """
        Sea-Surface Temperature was used as the target variable.
        SST is a continuous numerical value, so regression models were
        appropriate for this part of the project.
        """
    )

    st.write(
        """
        Three regression models were compared:
        """
    )

    st.markdown(
        """
        - Linear Regression
        - Unrestricted Decision Tree Regression
        - Limited-depth Decision Tree Regression
        """
    )

    st.write(
        """
        The data was divided into 80% training data and 20% testing data
        using a random state of 42. Root Mean Squared Error (RMSE) was
        used to compare the prediction error of the models.
        """
    )

    st.markdown(
        """
        **Model results:**

        - Linear Regression: Training RMSE = 1.87°C, Testing RMSE = 1.89°C
        - Unrestricted Decision Tree: Training RMSE = 0.00°C, Testing RMSE = 0.05°C
        - Limited-depth Decision Tree: Training RMSE = 0.37°C, Testing RMSE = 0.38°C
        """
    )

    st.write(
        """
        The unrestricted Decision Tree achieved the lowest testing RMSE
        and was therefore selected for the SST prediction tool in this
        Streamlit application.

        However, the unrestricted tree fitted the training data almost
        perfectly. This shows that the model is highly complex and its
        performance on genuinely new observations should be treated
        cautiously.
        """
    )

    st.info(
        "The machine-learning model predicts SST associated with a "
        "recorded observation. It does not predict whether a humpback "
        "whale will be present at a particular location."
    )


# Limitations of the Analysis

with st.expander("Limitations of the Analysis"):

    st.write(
        """
        There are several limitations that should be considered when
        interpreting the results of this project.
        """
    )

    st.markdown(
        """
        - The records represent recorded humpback whale observations rather
          than the total humpback whale population.

        - A greater number of observation records does not necessarily mean
          that a greater number of whales were present.

        - Observation numbers may be affected by survey effort, reporting
          effort, tourism and accessibility.

        - The dataset does not provide reliable information about locations
          where whales were searched for but not observed. It therefore
          cannot be used to calculate true whale presence or absence.

        - Some records were missing SST and SSS measurements. These records
          were excluded from the relevant environmental analyses rather than
          having values estimated.

        - Geographical location is important when interpreting seasonal SST.
          Higher SST associated with Winter observations does not mean that
          the entire North Pacific is warmer during Winter.

        - The hypothesis test contained very large sample sizes. Large sample
          sizes can result in very small p-values, so statistical significance
          was considered alongside descriptive statistics and visualisations.

        - The machine-learning models were evaluated using a random
          train/test split. Similar geographical or temporal observations
          may therefore have appeared in both datasets.

        - Relationships identified in this project show associations and
          should not be interpreted as evidence of causation.
        """
    )

    st.write(
        """
        A future improvement would be to evaluate the machine-learning model
        using completely different years or geographical regions to provide
        a stronger test of how well it generalises to new observations.
        """
    )


# Ethics and Data Governance

with st.expander("Ethics & Data Governance"):

    st.write(
        """
        The OBIS dataset contains environmental and wildlife observation
        information rather than personal information such as names,
        addresses or contact details.

        However, ethical considerations are still important because the
        dataset contains geographical information showing where wildlife
        has been recorded.
        """
    )

    st.write(
        """
        Wildlife location information should be handled responsibly.
        In this project, geographical coordinates are used to investigate
        broad patterns in the observation data rather than to encourage
        users to locate individual animals.
        """
    )

    st.write(
        """
        Another important ethical consideration is how the findings are
        communicated. Observation counts have not been described as direct
        measurements of whale abundance because reporting and observation
        effort may vary between different areas and seasons.
        """
    )

    st.write(
        """
        The relationships between season, SST, SSS and recorded observations
        are also described as associations rather than evidence that one
        variable directly causes changes in humpback whale distribution.
        """
    )

    st.write(
        """
        The original data source is acknowledged within the project and the
        original dataset is retained separately from the cleaned dataset.
        This allows the cleaning and analysis process to be checked and
        reproduced.
        """
    )


# Use of AI

with st.expander("Use of AI"):

    st.write(
        """
        I used AI, specifically ChatGPT, as a support tool at several
        stages of this project.
        """
    )

    st.markdown(
        """
        AI was used to assist with:

        - Identifying useful variables within the original dataset.
        - Troubleshooting Python errors.
        - Investigating missing and incorrect month values.
        - Troubleshooting machine-learning code.
        - Understanding statistical concepts such as hypothesis testing,
          p-values and RMSE.
        - Supporting the interpretation of analysis results.
        - Learning how to structure and develop this multipage Streamlit
          application.
        """
    )

    st.write(
        """
        AI-generated suggestions were not automatically assumed to be
        correct. Code was run and tested and interpretations were checked
        against the actual outputs produced from the dataset.
        """
    )

    st.write(
        """
        During the project I found that AI tools can sometimes provide
        incorrect suggestions, make assumptions or present inaccurate
        information confidently. I therefore used AI as a learning and
        troubleshooting tool rather than as a replacement for checking
        the analysis myself.

        Responsibility for the final code, analysis, interpretation and
        conclusions remained with me.
        """
    )


# Final Interpretation Note

st.divider()

st.info(
    "The findings presented in this dashboard describe patterns within "
    "recorded humpback whale observations. They should not be interpreted "
    "as direct measurements of humpback whale population or abundance."
)