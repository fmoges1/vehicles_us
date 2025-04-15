import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os

df = pd.read_csv('vehicles_us.csv')
# Debug: Check if file exists
if not os.path.exists("vehicles_us.csv"):
    st.error("CSV file not found. Please make sure it is included in the root directory.")
else:
    # Try loading the file safely
    try:
        df = pd.read_csv("vehicles_us.csv")
        st.success("CSV file loaded successfully!")

        # Check column types
        st.write("Column types:")
        st.write(df.dtypes)

        # Show a few rows
        st.write("Sample data:")
        st.write(df.head())
    except Exception as e:
        st.error(f"Error reading CSV: {e}")

# Try to coerce any weird types (especially object columns)
df = df.convert_dtypes()
df = df.infer_objects()

# Flatten any nested arrays (common cause)
for col in df.columns:
    df[col] = df[col].apply(lambda x: x[0] if isinstance(x, np.ndarray) and len(x) == 1 else x)
    df[col] = df[col].apply(lambda x: str(x) if isinstance(x, np.ndarray) else x)

# Cast known numeric columns to float (optional)
numeric_cols = ['price', 'odometer']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')


        
#df = pd.read_csv('vehicles_us.csv')
#df['price'] = pd.to_numeric(df['price'], errors='coerce')  # Ensure price is float

#st.write("Data types")
#st.write(df.dtypes)

# Coerce all columns to standard NumPy/Pandas types
#df = df.convert_dtypes()
#df = df.infer_objects()

# Further coerce numeric columns to ensure no mixed or extension types
#for col in df.select_dtypes(include='number').columns:
  #  df[col] = pd.to_numeric(df[col], errors='coerce')

# Optional: display types to verify
#st.write("Cleaned data types:")
#st.write(df.dtypes)


# Vehicle Listings Data Viewer
#st.header('Vehicle Listings Data Viewer')
#st.dataframe(df)

# Add some basic statistics
#st.subheader('Quick Stats')
#st.write(f"Total listings: {len(df)}")
#st.write(f"Date range: {df['date_posted'].min()} to {df['date_posted'].max()}")
