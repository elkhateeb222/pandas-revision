import streamlit as st ##streamlit run app/app.py
import pandas as pd
from altair.vegalite.v4.api import Chart


st.markdown(
    "<h4 style='color:orange; font-family:Book Antiqua; text-align:center; font-style:italic;'>"
    "📊 This dashboard provides an interactive analysis of the Egyptian real estate market 🏘️📍"
    "</h4>",
    unsafe_allow_html=True
)
st.markdown(
    "<h2 style='color:white; font-family:Book Antiqua; text-align:center;'>"
    "🏠 Houses Analysis in Egypt 🇪🇬"
    "</h2>",
    unsafe_allow_html=True
)
if st.button("Go to dashboard"):
    st.switch_page("pages/dashboard.py")