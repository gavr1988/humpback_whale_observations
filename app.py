import streamlit as st
import pandas as pd

#Making the browser tab and page layout

st.set_page_config(
    page_title="Humpback Whale Analytics",
    page_icon="🐋",
    layout="wide"
)

#Loading the cleaned whale observation dataset. 
# @st.cache_data tells streamlit to remember the loaded data
# this prevents the reading of the csv each time the app reruns. 

@st.cache_data
def load_data():
    df = pd.read_csv("whale_data_cleaned.csv")
    return df

#Now the function will be called to load and store the cleaned data in a df
df = load_data()

#Main Page Title
st.title("North Pacific Humpback Whale Analytics")

#The Research Question

st.subheader("Research Question")
st.write("How do recorded North Pacific Humpback Whale observations vary by season and sea surface temperature between 2010 and 2025?")

# Calculate the headline statistics for the homepage.
total_records = len(df)

earliest_year = int(df["date_year"].min())
latest_year = int(df["date_year"].max())

winter_percentage = (
    (df["season"] == "Winter").mean() * 100
)

mean_sst = df["sst"].mean()


# Create four columns for the headline statistics.
col1, col2, col3, col4 = st.columns(4)


# Display the statistics as metric cards.
col1.metric(
    "Recorded Observations",
    f"{total_records:,}"
)

col2.metric(
    "Analysis Period",
    f"{earliest_year}–{latest_year}"
)

col3.metric(
    "Winter Observations",
    f"{winter_percentage:.2f}%"
)

col4.metric(
    "Mean SST",
    f"{mean_sst:.2f}°C"
)

#Putting a divider between the headline statistics and the rest of the page content.
st.divider()

#Why I chose this project

st.subheader("Why I chose this project")
st.write ("I chose to investigate Humpback Whale after a recent trip to Alaska, where I had the opportuinity to see humpback whales in their natural environment. This experience inspired me to explore how recorded humpback whale observations vary across the north pacidic and are associated with environmental conditions such as Sea Surface Temperature.")

