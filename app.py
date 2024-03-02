import streamlit as st
import pandas as pd


# Read CSV data into a DataFrame
df = pd.read_csv("output.csv")
# Fill NaN values with a specified value, for example, 0
df.fillna(0, inplace=True)

col1, col2, col3 = st.columns([4, 10, 4])


col1.write("#### Filters")
Years = df["Year"]
option0 = col1.selectbox("Since Year", tuple(Years.unique()))
Data0 = df[df["Year"] >= option0]

Tickers = Data0["Ticker"]
option = col1.selectbox("Ticker", tuple(Tickers.unique()))
Data = Data0[Data0["Ticker"] == option]


Position = Data["Position"]
option2 = col1.selectbox("Position", tuple(Position.unique()))
Data2 = Data[Data["Position"] == option2]

# Salary growth
col2.write("# Salary Growth")
columns_to_extract = ["Name", "Position", "Salary", "Year"]
extracted_df = Data2[columns_to_extract].copy()


col2.write(f"### {option2} salary growth since {option0}")
extracted_df = extracted_df[extracted_df["Position"] != 0]
# extracted_df
col2.bar_chart(extracted_df, y="Salary", x="Year")

col3.write("#### Total Compensation")
columns_to_extract2 = ["Year", "Ticker", "Name", "Total"]
extracted_df2 = Data2[columns_to_extract2].copy()
extracted_df2.set_index("Year")
col3.dataframe(extracted_df2, hide_index=True)
