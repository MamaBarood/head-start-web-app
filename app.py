
def load_data():
    df = pd.read_excel("HS data for web app 2024.xlsx")
    st.write("Column names in Excel:", list(df.columns))  # <-- Add this line
    ...