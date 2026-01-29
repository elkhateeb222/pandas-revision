import streamlit as st
import pandas as pd
df=pd.read_csv("houses_data_v2.csv")






st.markdown("<h1 style= 'color:white; font-family:book antiqua;text-align:center;'> 📊 Dashboard </h1>",unsafe_allow_html=True)

city = st.sidebar.multiselect(
    label="City",
    options=df["City"].unique(),
    
    default=df["City"].unique()
    
)
furnished=st.sidebar.multiselect(
    label="Furnished",
    options=df["Furnished"].unique(),
    default=df["Furnished"].unique()
)
for_rent=st.sidebar.multiselect(
    label="For_rent",
    options=df["For_rent"].unique(),
    default=df["For_rent"].unique()
)

filtered_df=df.query("City==@city and Furnished ==@furnished and For_rent==@for_rent")

st.dataframe(filtered_df)
total_units=df["House_Type"].shape[0]

no_of_house_types=df["House_Type"].nunique()

avg_size=round(float(df["Size"].mean()),1)

avg_meter_price=round(float(df["price_of_meter"].mean()),1)

avg_of_bathrooms=round(float(df["Bathrooms"].mean()))
