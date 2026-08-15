import streamlit as st
import pandas as pd

#In this section I have consulted ChatGPT to help me with the code for a map. I ahve also used the streamlit documentation to help me with the code.

# Configure this page.
st.set_page_config(
    page_title="Observation Map",
    page_icon="🗺️",
    layout="wide"
)


# Load the cleaned whale observation dataset.
@st.cache_data
def load_data():
    df = pd.read_csv("whale_data_cleaned.csv")
    return df


df = load_data()


# Page title.
st.title("Humpback Whale Observation Map")

st.write(
    "Explore where humpback whale observations were recorded "
    "across the North Pacific between 2010 and 2025."
)



# FILTERS


st.subheader("Filters")


# Create a season dropdown.
season_options = [
    "All",
    "Winter",
    "Spring",
    "Summer",
    "Autumn"
]

selected_season = st.selectbox(
    "Select a season:",
    season_options
)


# Create a year dropdown.
year_options = ["All"] + sorted(
    df["date_year"].dropna().astype(int).unique().tolist()
)

selected_year = st.selectbox(
    "Select a year:",
    year_options
)


# Filtering the Data


# Start with the full dataset.
filtered_df = df.copy()


# Filter by season if the user has selected one.
if selected_season != "All":
    filtered_df = filtered_df[
        filtered_df["season"] == selected_season
    ]


# Filter by year if the user has selected one.
if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["date_year"] == selected_year
    ]



# Map Information


st.subheader("Recorded Observation Locations")


# Show how many records are currently being displayed.
st.metric(
    "Records Displayed",
    f"{len(filtered_df):,}"
)


# Remove any records without coordinates before mapping.
map_df = filtered_df.dropna(
    subset=["decimalLatitude", "decimalLongitude"]
)


# Display the observation locations on a map.
st.map(
    map_df,
    latitude="decimalLatitude",
    longitude="decimalLongitude"
)


#  This note will explain the interpretation of the map.
st.info(
    "Each point represents a recorded humpback whale observation. "
    "The number of points should not be interpreted as a direct measure of humpback whale population or abundance."
)