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

