import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="UK Housing Market Dashboard",
    layout="wide"
)

st.title("🏠 UK Housing Market Dashboard")

# -----------------------------
# Load Data (Cloud Safe Path)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(BASE_DIR, "data", "processed", "cleaned_housing.csv")

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    return df

df = load_data(data_path)

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

regions = sorted(df['RegionName'].dropna().unique())
selected_region = st.sidebar.selectbox(
    "Select Region",
    options=["All Regions"] + regions
)

years = sorted(df['Year'].dropna().unique())
selected_year = st.sidebar.selectbox(
    "Select Year",
    options=["All Years"] + years
)

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df.copy()

if selected_region != "All Regions":
    filtered_df = filtered_df[filtered_df['RegionName'] == selected_region]

if selected_year != "All Years":
    filtered_df = filtered_df[filtered_df['Year'] == selected_year]

# -----------------------------
# KPI Metrics
# -----------------------------
col1, col2 = st.columns(2)

avg_price = filtered_df['AveragePrice'].mean()
sales_volume = filtered_df['SalesVolume'].mean()

col1.metric(
    "Average Price (£)",
    f"{int(avg_price):,}" if pd.notna(avg_price) else "N/A"
)

col2.metric(
    "Average Sales Volume",
    f"{int(sales_volume):,}" if pd.notna(sales_volume) else "N/A"
)

st.markdown("---")

# -----------------------------
# Price Trend Chart
# -----------------------------
st.subheader("📈 Average House Price Trend")

trend_df = (
    filtered_df
    .groupby('Date')['AveragePrice']
    .mean()
    .reset_index()
)

fig_trend = px.line(
    trend_df,
    x='Date',
    y='AveragePrice',
    title="Average Price Over Time"
)

st.plotly_chart(fig_trend, use_container_width=True)

# -----------------------------
# Property Type Comparison
# -----------------------------
st.subheader("🏘️ Average Price by Property Type")

property_cols = [
    'DetachedPrice',
    'SemiDetachedPrice',
    'TerracedPrice',
    'FlatPrice'
]

prop_df = filtered_df[property_cols].mean().reset_index()
prop_df.columns = ['Property Type', 'Average Price']

fig_bar = px.bar(
    prop_df,
    x='Property Type',
    y='Average Price',
    title="Average Price by Property Type"
)

st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")
st.caption("Built with Streamlit • UK Housing Data Analysis")