import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("UK Housing Market Dashboard")

# Load data
df = pd.read_csv("data/processed/cleaned_housing.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

# Sidebar filters
st.sidebar.header("Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df['Year'].unique(), reverse=True)
)

regions = st.sidebar.multiselect(
    "Select Region",
    sorted(df['RegionName'].unique())
)

filtered_df = df[(df['Year'] == selected_year) & (df['RegionName'].isin(regions))]

# Stop app if no region selected (prevents errors)
if len(regions) == 0:
    st.warning("Please select at least one region from the sidebar.")
    st.stop()

# KPI Metrics
col1, col2, col3 = st.columns(3)

avg_price = filtered_df['AveragePrice'].mean()
avg_sales = filtered_df['SalesVolume'].mean()

col1.metric("Average Price (£)", f"{avg_price:,.0f}")
col2.metric("Average Sales Volume", f"{avg_sales:,.0f}")
col3.metric("Regions Selected", len(regions))

st.markdown("---")

# Price Trend (UK overall)
trend = df.groupby('Date')['AveragePrice'].mean().reset_index()
fig1 = px.line(
    trend, x='Date', y='AveragePrice',
    title="UK Average House Price Trend Over Time"
)
st.plotly_chart(fig1, use_container_width=True)

# Regional Comparison
region_prices = filtered_df.groupby('RegionName')['AveragePrice'].mean().reset_index()
fig2 = px.bar(
    region_prices, x='RegionName', y='AveragePrice',
    title="Average Price by Selected Regions"
)
st.plotly_chart(fig2, use_container_width=True)

# Property Type Comparison
property_cols = ['DetachedPrice','SemiDetachedPrice','TerracedPrice','FlatPrice']
avg_prices = df[property_cols].mean().reset_index()
avg_prices.columns = ['PropertyType','Price']
fig3 = px.bar(
    avg_prices, x='PropertyType', y='Price',
    title="Average Price by Property Type"
)
st.plotly_chart(fig3, use_container_width=True)

# Sales Volume Trend
sales_trend = df.groupby('Date')['SalesVolume'].mean().reset_index()
fig4 = px.line(
    sales_trend, x='Date', y='SalesVolume',
    title="Housing Sales Volume Over Time"
)
st.plotly_chart(fig4, use_container_width=True)