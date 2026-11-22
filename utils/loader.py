import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path="data/clean_gadget.csv"):
    return pd.read_csv(path)