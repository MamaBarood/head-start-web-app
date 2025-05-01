
import streamlit as st
import pandas as pd
from difflib import get_close_matches

# Load data
def load_data():
    df = pd.read_excel("HS data for web app 2024.xlsx", header=1)
    df = df.rename(columns={
        "program_name": "program_name",
        "state": "state",
        "head_start_slots": "head_start_slots",
        "funding_per_pupil_base": "funding_per_pupil_base",
        "Geog adjusted HS Base $PP using CWIFT": "geo_adjusted_funding",
        "pct_below_100_fpl": "pct_below_100_fpl",
        "pct_foster_care": "pct_foster_care",
        "pct_homeless": "pct_homeless",
        "pct_non_english": "pct_non_english",
        "pct_on_iep": "pct_on_iep"
    })
    columns_needed = [
        "program_name", "state", "head_start_slots", "funding_per_pupil_base",
        "geo_adjusted_funding", "pct_below_100_fpl", "pct_foster_care",
        "pct_homeless", "pct_non_english", "pct_on_iep"
    ]
    return df[columns_needed].dropna(subset=["program_name"])

# Load dataset
df = load_data()

st.title("Head Start Program Data Explorer")

# User input
program_input = st.text_input("Enter your program name (or a few words from it):")

if program_input:
    matches = get_close_matches(program_input, df["program_name"], n=5, cutoff=0.4)

    if len(matches) == 0:
        st.warning("No similar program names found.")
    else:
        selected_program = st.selectbox("Select your program:", matches)
        program_data = df[df["program_name"] == selected_program].iloc[0]
        state_data = df[df["state"] == program_data["state"]]

        def median_or_na(series):
            return round(series.median(), 2) if not series.empty else "N/A"

        # Build output table
        output = pd.DataFrame({
            "Metric": [
                "Head Start slots",
                "Funding per pupil (Base)",
                "Geo-adjusted funding (CWIFT)",
                "% below 100% poverty line",
                "% foster care",
                "% homeless",
                "% non-English speaking",
                "% on IEP"
            ],
            "Your Program": [
                program_data["head_start_slots"],
                program_data["funding_per_pupil_base"],
                program_data["geo_adjusted_funding"],
                program_data["pct_below_100_fpl"],
                program_data["pct_foster_care"],
                program_data["pct_homeless"],
                program_data["pct_non_english"],
                program_data["pct_on_iep"]
            ],
            "State Median": [
                median_or_na(state_data["head_start_slots"]),
                median_or_na(state_data["funding_per_pupil_base"]),
                median_or_na(state_data["geo_adjusted_funding"]),
                median_or_na(state_data["pct_below_100_fpl"]),
                median_or_na(state_data["pct_foster_care"]),
                median_or_na(state_data["pct_homeless"]),
                median_or_na(state_data["pct_non_english"]),
                median_or_na(state_data["pct_on_iep"])
            ],
            "US Median": [
                median_or_na(df["head_start_slots"]),
                median_or_na(df["funding_per_pupil_base"]),
                median_or_na(df["geo_adjusted_funding"]),
                median_or_na(df["pct_below_100_fpl"]),
                median_or_na(df["pct_foster_care"]),
                median_or_na(df["pct_homeless"]),
                median_or_na(df["pct_non_english"]),
                median_or_na(df["pct_on_iep"])
            ]
        })

        st.subheader("Comparison Table")
        st.dataframe(output.set_index("Metric"))
