import streamlit as st

#Making the browser tab and page layout
st.set_page_config(
    page_title="Humpback Whale Analytics",
    page_icon="🐋",
    layout="wide"
)

#Main Page Title
st.title("North Pacific Humpback Whale Analytics")

#The Research Question

st.subheader("Research Question")
st.write("How do recorded North Pacific Humpback Whale observations vary by season and sea surface temperature between 2010 and 2025?")

