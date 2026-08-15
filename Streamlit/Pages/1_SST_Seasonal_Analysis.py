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


# Find the earliest and latest years in the dataset.
min_year = int(df["date_year"].min())
max_year = int(df["date_year"].max())


# Create a year-range slider.
selected_years = st.slider(
    "Select a year range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)



#Filtering the data
#I will be utilising a slider to filter the data.

# Start with records inside the selected year range.
filtered_df = df[
    df["date_year"].between(
        selected_years[0],
        selected_years[1]
    )
].copy()


# If the user selects a specific season, keep only records from that season.
if selected_season != "All":
    filtered_df = filtered_df[
        filtered_df["season"] == selected_season
    ]



# Summary Statistics


st.subheader("Summary Statistics")


# Calculate statistics from the filtered dataset.
total_records = len(filtered_df)

mean_sst = filtered_df["sst"].mean()

median_sst = filtered_df["sst"].median()

sst_std = filtered_df["sst"].std()


# Create four dashboard columns.
col1, col2, col3, col4 = st.columns(4)


# Display the filtered statistics.
col1.metric(
    "Recorded Observations",
    f"{total_records:,}"
)

col2.metric(
    "Mean SST",
    f"{mean_sst:.2f}°C"
)

col3.metric(
    "Median SST",
    f"{median_sst:.2f}°C"
)

col4.metric(
    "SST Standard Deviation",
    f"{sst_std:.2f}°C"
)