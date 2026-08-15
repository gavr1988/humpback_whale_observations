import streamlit as st
import pandas as pd


# Configure this page.
st.set_page_config(
    page_title="SST & Seasonal Analysis",
    page_icon="🌊",
    layout="wide"
)


# Load the cleaned whale observation dataset.

@st.cache_data
def load_data():
    df = pd.read_csv("whale_data_cleaned.csv")
    return df


df = load_data()


# Page title.
st.title("SST & Seasonal Analysis")

st.write(
    "Explore how recorded humpback whale observations and "
    "sea-surface temperature vary by season and year."
)

#Adding Filters

st.subheader("Filters")


# Create a season filter.
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
