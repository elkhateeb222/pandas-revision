import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config("Dashboard",'📊', layout="wide")


df=pd.read_excel("data/cleaned data/cleaned_data.xlsx")





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

#kpi---->5
total_units=filtered_df["House_Type"].shape[0]
no_of_house_types=filtered_df["House_Type"].nunique()
avg_size=round(float(filtered_df["Size"].mean()),1)
avg_meter_price=round(float(filtered_df["price_of_meter"].mean()),1)
avg_of_bathrooms=round(float(filtered_df["Bathrooms"].mean()))




kpi1,kpi2,kpi3,kpi4,kpi5=st.columns(5,border=True)
kpi1.markdown(f"<h4 style='color:red;'>Total Units \n\n{total_units}</h1>",unsafe_allow_html=True)
kpi2.markdown(f"<h4 style='color:red'> no of house types \n\n\n\n{no_of_house_types} </h1>",unsafe_allow_html=True)
kpi3.markdown(f"<h4 style='color:red'> avg size \n\n\n\n{avg_size} </h1>",unsafe_allow_html=True)
kpi4.markdown(f"<h4 style='color:red'> avg meter price \n\n\n\n{avg_meter_price} </h1>",unsafe_allow_html=True)
kpi5.markdown(f"<h4 style='color:red'> avg of bathrooms \n\n\n\n{avg_of_bathrooms} </h1>",unsafe_allow_html=True)

fig = px.treemap(
    filtered_df,
    title="Tree Map Of Cities (Size varies According To Price)",
    path=[px.Constant("egypt"), "City", "Region"],
    values="Price",
    width=2000,height=700
)

fig.update_traces(
    hovertemplate=
    "<b>%{label}</b><br>" +
    "Price: %{value:,.0f}<extra></extra>"
)


st.plotly_chart(fig)

total_price_by_house_type=filtered_df.groupby("House_Type")["Price"].sum().to_frame().reset_index()
avg_price_by_house_type=filtered_df.groupby("House_Type")["Price"].mean().astype(int).to_frame().reset_index()
fig1,fig2=st.columns(2)

pie_total_price=px.pie(total_price_by_house_type,names="House_Type",values="Price",color_discrete_sequence=px.colors.qualitative.Dark24,title="Market share of each house type")
histo_avg_price=px.histogram(avg_price_by_house_type,x="House_Type",y="Price",color="Price",color_discrete_sequence=px.colors.qualitative.Dark24,log_y=True,title="avarage price of each house type")
fig1.plotly_chart(pie_total_price)
fig2.plotly_chart(histo_avg_price)

sun_of_egypt=px.sunburst(filtered_df,path=[px.Constant("Egypt"),"City","Region"],values="Price",
            color_discrete_sequence=px.colors.qualitative.Dark24,title="sunburst of egypt (size varies according to price)")
st.plotly_chart(sun_of_egypt,width=6000,height=600)