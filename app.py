
import streamlit as st
import pandas as pd
from difflib import get_close_matches

# Load data and show column names for debugging
def load_data():
    df = pd.read_excel("HS data for web app 2024.xlsx", header=1)
    st.write("📋 Excel Column Names:")
    st.write(df.columns.tolist())
    return df

# Load dataset
df = load_data()

st.title("Head Start Program Data Explorer")

# User input (disabled further logic until we get the correct column names)
program_input = st.text_input("Enter your program name (or a few words from it):")

if program_input:
    st.info("Once we verify column names, functionality will be restored.")
