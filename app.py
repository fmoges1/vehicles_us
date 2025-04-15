import streamlit as st
import pandas as pd
import plotly.express as px
#import numpy as np

df = pd.read_csv('vehicles_us.csv')

# Vehicle Listings Data Viewer
st.header('Vehicle Listings Data Viewer')
df["price"] = df["price"].astype(np.dtype("float64"))
st.dataframe(df)

# Add some basic statistics
st.subheader('Quick Stats')
st.write(f"Total listings: {len(df)}")
st.write(f"Date range: {df['date_posted'].min()} to {df['date_posted'].max()}")
