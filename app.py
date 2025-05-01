import streamlit as st
import pandas as pd
from difflib import get_close_matches

# Load data
def load_data():
    df = pd.read_excel("cleaned_hs_data.xlsx")
    columns_needed = [
        "program_name", "state", "head_start_slots", "funding_per_pupil_base",
        "geo_adjusted_funding", "pct_below_100_fpl", "pct_foster_care",
        "pct_homeless", "pct_non_english", "pct_on_iep"
    ]
    return df[columns_needed].dropna(subset=["program_name"])

# Load dataset
df = load_data()

st.title("Head Start Program Data Explorer")