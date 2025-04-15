import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('vehicles_us.csv')
df['price'] = pd.to_numeric(df['price'], errors='coerce')  # Ensure price is float

st.write("Data types")
st.write(df.dtypes)

# Vehicle Listings Data Viewer
st.header('Vehicle Listings Data Viewer')

st.dataframe(df)

# Add some basic statistics
st.subheader('Quick Stats')
st.write(f"Total listings: {len(df)}")
st.write(f"Date range: {df['date_posted'].min()} to {df['date_posted'].max()}")
