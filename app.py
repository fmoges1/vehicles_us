import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os

df = pd.read_csv('vehicles_us.csv')

# Read CSV as raw strings (no dtype inference)
#df = pd.read_csv('vehicles_us.csv', dtype=str, low_memory=False)


# Vehicle Listings Data Viewer
#st.header('Vehicle Listings Data Viewer')
#st.dataframe(df)

# Add some basic statistics
#st.subheader('Quick Stats')
#st.write(f"Total listings: {len(df)}")
#st.write(f"Date range: {df['date_posted'].min()} to {df['date_posted'].max()}")

# Main header
st.header('Vehicle Types by Price Analysis')

# 1. Show average price by vehicle type
st.subheader('Average Price by Vehicle Type')
avg_price_by_type = df.groupby('type')['price'].mean().sort_values(ascending=False).round(2)
st.write(avg_price_by_type)


# 2. Show price distribution by type
st.subheader('Price Distribution by Type')
st.write("Minimum prices:")
min_prices = df.groupby('type')['price'].min().sort_values(ascending=False)
st.write(min_prices)

st.write("\nMaximum prices:")
max_prices = df.groupby('type')['price'].max().sort_values(ascending=False)
st.write(max_prices)

# Visualization of Price Distribution
st.subheader('Price Distribution Visualization')
st.bar_chart(df.groupby('type')['price'].mean())


# Vehicle Price Distribution Analysis
# Create header
st.header('Vehicle Price Distribution Analysis')

# Create Plotly Express histogram
fig = px.histogram(df, 
  x='price',
  nbins=50,
  title='Distribution of Vehicle Prices',
  labels={'price': 'Price ($)'},
  color_discrete_sequence=['#1f77b4'])

# Customize layout
fig.update_layout(
    bargap=0.1,
    xaxis_title='Vehicle Price ($)',
    yaxis_title='Number of Listings',
    hovermode='x unified'
)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Add interactive filters
st.subheader('Filter by Vehicle Type')
selected_type = st.selectbox(
    'Select vehicle type to analyze:',
    options=['All'] + sorted(df['type'].unique().tolist()))


if selected_type != 'All':
    filtered_df = df[df['type'] == selected_type]
    fig2 = px.histogram(filtered_df, 
        x='price',
        nbins=30,
        title=f'Price Distribution for {selected_type}',
        labels={'price': 'Price ($)'},
        color_discrete_sequence=['#ff7f0e'])
    st.plotly_chart(fig2, use_container_width=True)



# header
st.header('Vehicle Price vs. Mileage')

# Create basic scatter plot
fig = px.scatter(
    df,
    x='odometer',
    y='price',
    title='Vehicle Prices by Mileage'
)

# Display in Streamlit
st.plotly_chart(fig)


st.header('Vehicle Data Explorer')

# Create checkbox
show_plot = st.checkbox('Show Scatter Plot (Price vs. Mileage)', value=True)

if show_plot:
    # Display scatter plot when checked
    fig = px.scatter(
        df,
        x='odometer',
        y='price',
        title='Price vs. Mileage',
        labels={'odometer': 'Mileage (miles)', 'price': 'Price ($)'}
    )
    st.plotly_chart(fig)
else:
    # Display raw data when unchecked
    st.write("Raw Data:")
    st.dataframe(df)

