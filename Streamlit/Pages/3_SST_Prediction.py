import streamlit as st
import pandas as pd
from pathlib import Path
from sklearn.tree import DecisionTreeRegressor


#Page Configuration

st.set_page_config(
    page_title="SST Prediction",
    page_icon="📈",
    layout="wide"
)

# Loading the cleaned data.


# This page is stored inside the "pages" folder.
# The cleaned CSV is stored one folder above it in the main Streamlit folder.

data_path = (
    Path(__file__).resolve().parents[1]
    / "whale_data_cleaned.csv"
)


# Cache the dataset so Streamlit does not need to reload the CSV after every interaction.
@st.cache_data
def load_data():

    df = pd.read_csv(data_path)

    return df


df = load_data()



# PREPARE THE M-L Data


# These are the same predictor variables used in the Jupyter Notebook.

features = [
    "date_year",
    "month",
    "decimalLatitude",
    "decimalLongitude"
]


# Remove any records that are missing one of thepredictor variables or the SST target value.

model_df = df.dropna(
    subset=features + ["sst"]
).copy()


# X contains the predictor variables as detailed in the Jupyter notebook.

X = model_df[features]


# y contains the target variable that the model will learn to predict.

y = model_df["sst"]

# Train the model


# Cache the trained model so that Streamlit does not retrain it every time the user changes an input.

@st.cache_resource
def train_model(X, y):

    # This is the unrestricted Decision Tree model used in the Jupyter Notebook.
    
    # max_depth=None means that no maximum tree depth has been specified.

    model = DecisionTreeRegressor(
        max_depth=None,
        random_state=42
    )

    # Train the model using the cleaned data.

    model.fit(X, y)

    return model


model = train_model(X, y)



# Page Title and Introduction


st.title("Sea-Surface Temperature Prediction")


st.write(
    "This page uses a machine-learning model to estimate the sea-surface temperature associated with a recorded humpback whale observation."
)


st.write(
    "The prediction is based on the year, month, latitude and longitude entered below."
)



# User Input


st.subheader("Enter Observation Information")


# Find the year range contained in the dataset.

min_year = int(model_df["date_year"].min())
max_year = int(model_df["date_year"].max())


# Put Year and Month next to each other.

col1, col2 = st.columns(2)


with col1:

    selected_year = st.number_input(
        "Year",
        min_value=min_year,
        max_value=max_year,
        value=2020,
        step=1
    )


with col2:

    selected_month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=7,
        step=1
    )


# Find the geographical range contained within the cleaned dataset.

min_latitude = float(model_df["decimalLatitude"].min())
max_latitude = float(model_df["decimalLatitude"].max())

min_longitude = float(model_df["decimalLongitude"].min())
max_longitude = float(model_df["decimalLongitude"].max())


# Put Latitude and Longitude next to each other.

col3, col4 = st.columns(2)


with col3:

    selected_latitude = st.number_input(
        "Latitude",
        min_value=min_latitude,
        max_value=max_latitude,
        value=55.0
    )


with col4:

    selected_longitude = st.number_input(
        "Longitude",
        min_value=min_longitude,
        max_value=max_longitude,
        value=-135.0
    )



# Making the Prediction


if st.button("Predict SST"):

    # Create a DataFrame containing one row.
    # This row contains the values entered by the user.

    prediction_data = pd.DataFrame(
        {
            "date_year": [selected_year],
            "month": [selected_month],
            "decimalLatitude": [selected_latitude],
            "decimalLongitude": [selected_longitude]
        }
    )


    # Use the trained Decision Tree to predict SST.

    predicted_sst = model.predict(
        prediction_data
    )[0]


   
    # Displaying the result
   
    st.subheader("Prediction Result")


    st.metric(
        "Estimated Sea-Surface Temperature",
        f"{predicted_sst:.2f}°C"
    )



# Model Information


st.divider()


st.subheader("Information about the Model")


st.write(
    "The prediction is generated using an unrestricted Decision Tree regression model. The model uses year, month, latitude and longitude as predictor variables and sea-surface temperature as the target variable."
)


st.write(
    "During evaluation in the Jupyter Notebook, the unrestricted Decision Tree achieved a training RMSE of approximately 0.00°C and a testing RMSE of approximately 0.05°C."
)


st.write(
    "The testing RMSE was the lowest of the three models evaluated in the project. However, the perfect training fit shows that the model is highly complex."
)


st.warning(
    "The model was evaluated using a random training and testing split. Records with similar geographical and temporal characteristics may therefore have appeared in both datasets. "
    "Its performance on genuinely new years or geographical areas should be treated cautiously."
)


st.info(
    "This model predicts sea-surface temperature associated with recorded humpback whale observations. It does not predict whether a humpback whale will be present at a particular location."
)