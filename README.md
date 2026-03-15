# 🏠 UK House Price Analysis & Interactive Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-blue)
![Plotly](https://img.shields.io/badge/Plotly-Visualisation-darkblue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

An **end-to-end Data Analytics project** analysing the UK housing market using **data cleaning, exploratory data analysis, feature engineering, and an interactive Streamlit dashboard**.

This project demonstrates a complete **real-world data science workflow**:

Data Collection → Data Cleaning → Feature Engineering → Exploratory Analysis → Visualization → Interactive Dashboard

---

# 🌐 Live Dashboard

Explore the deployed interactive dashboard:

👉 https://uk-house-price-analysis-dqzntjmkycmty2379wdnkp.streamlit.app/

The dashboard allows users to explore UK housing data through **interactive filters and dynamic visualisations**.

---

# 🎯 Project Objective

The goal of this project is to analyse trends in the **UK housing market** and build an interactive dashboard that enables users to explore:

• House price trends over time  
• Regional price differences  
• Property type comparisons  
• Key housing market insights  

The project demonstrates practical skills in **data cleaning, exploratory data analysis, and dashboard development**, which are commonly used in real-world data science roles.

---

# 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualisation | Plotly |
| Dashboard Framework | Streamlit |
| Notebook Environment | Jupyter Notebook |
| Development Environment | VS Code |
| Version Control | Git & GitHub |

---

# 🔄 Data Science Workflow

This project follows a typical **data analytics pipeline used in production systems**.

```
Raw Dataset
     ↓
Data Cleaning & Processing
     ↓
Feature Engineering
     ↓
Exploratory Data Analysis
     ↓
Interactive Dashboard
```

---

# 📥 Data Collection

The dataset contains UK housing market data including:

• Sale price  
• Property type  
• Region  
• Transaction date  

The dataset was prepared and structured to support time-series and regional analysis.

---

# 🧹 Data Cleaning & Processing

Data preprocessing was performed using **Pandas** to ensure high-quality analysis.

Steps performed:

• Removed missing values  
• Converted date columns to datetime format  
• Extracted year feature for time analysis  
• Standardised property type categories  
• Aggregated regional statistics  

The cleaned dataset is stored for efficient loading within the dashboard.

Output dataset:

```
data/processed/cleaned_housing.csv
```

---

# ⚙️ Feature Engineering

Feature engineering was applied to enrich the dataset and prepare it for analysis and potential machine learning tasks.

Engineered features include:

• Extracting **year** from transaction dates for time-series analysis  
• Calculating **regional average prices**  
• Encoding property type categories for structured analysis  
• Aggregating statistics to improve dashboard performance  

Example engineered features:

| Feature | Description |
|------|------|
| year | Extracted from transaction date |
| avg_price_region | Average price by region |
| property_type_encoded | Numerical encoding of property type |

Feature engineering allows the dataset to be used for **advanced analytics and predictive modelling**.

---

# 🔍 Exploratory Data Analysis (EDA)

EDA was performed using **Jupyter Notebook** to uncover patterns and trends in the housing dataset.

Key questions explored:

• How have UK house prices changed over time?  
• Which regions have the highest average house prices?  
• Which property types are the most expensive?  

Visualisations produced during EDA include:

• Time-series price trends  
• Regional price comparisons  
• Property type price distributions  

EDA notebook:

```
notebooks/eda.ipynb
```

---

# 🤖 Predictive Modelling (Extension)

Although the primary focus of this project is analytics and visualisation, the dataset can also support **predictive modelling for house price estimation**.

Possible modelling approaches include:

• Linear Regression  
• Random Forest Regression  
• Gradient Boosting Models  

Potential input features:

- region  
- property type  
- year  
- historical regional average price  

Target variable:

- house price

This extension demonstrates how the project can evolve from **data analytics into machine learning applications**.

---

# 📊 Model Comparison

Different machine learning models can be evaluated to determine the most accurate house price prediction approach.

| Model | Strength |
|------|------|
| Linear Regression | Simple baseline model |
| Random Forest | Handles non-linear relationships |
| Gradient Boosting | High predictive performance |

Comparing models allows selection of the algorithm that best captures housing market patterns.

---

# 📈 Evaluation Metrics

Regression models used for house price prediction can be evaluated using standard performance metrics.

| Metric | Description |
|------|------|
| MAE | Mean Absolute Error |
| RMSE | Root Mean Squared Error |
| R² Score | Explained variance of the model |

These metrics measure how accurately the model predicts property prices.

---

# 📊 Dashboard Development

An **interactive Streamlit dashboard** was developed to enable users to explore the housing dataset dynamically.

The dashboard includes:

### KPI Metrics

• Average UK House Price  
• Highest Price Region  
• Most Expensive Property Type  

### Interactive Filters

Users can filter data by:

• Region  
• Year  

### Visualisations

Interactive charts built with **Plotly**:

• House price trends over time  
• Average price by region  
• Average price by property type  

These visualisations allow users to quickly identify housing market patterns.

---

# 📈 Example Dashboard Workflow

```
User opens dashboard
        ↓
Select region and year filters
        ↓
Dashboard updates visualisations
        ↓
User explores housing market trends
```

---

# 📊 Key Insights

Analysis of the dataset reveals several housing market trends:

• UK house prices show a **long-term upward trend**  
• Large **regional price disparities** exist  
• **Detached houses consistently have the highest average price**  
• High-value regions dominate housing market prices  

---

# 🧩 Modular Project Design

The project follows a modular data science structure:

```
data/        → processed datasets
notebooks/   → exploratory analysis
dashboard/   → Streamlit dashboard application
```

This modular structure separates:

• data preparation  
• analysis notebooks  
• production dashboard code  

Such separation improves **maintainability, scalability, and reproducibility**.

---

# ⚡ Performance Considerations

To maintain dashboard responsiveness:

• Preprocessed datasets are used for faster loading  
• Aggregated statistics reduce computation time  
• Plotly ensures efficient interactive visualisation  

Future performance improvements may include:

• Streamlit caching  
• Optimised data loading  
• Scalable cloud data storage

---

# ▶️ Run Locally

Clone repository:

```
git clone https://github.com/premnadh/uk-house-price-analysis.git
```

Navigate into project:

```
cd uk-house-price-analysis
```

Install dependencies:

```
pip install -r requirements.txt
```

Run dashboard:

```
streamlit run dashboard/app.py
```

The dashboard will open automatically in your browser.

---

# 📂 Project Structure

```
uk-house-price-analysis
│
├── dashboard
│   └── app.py
│
├── data
│   └── processed
│       └── cleaned_housing.csv
│
├── notebooks
│   └── eda.ipynb
│
├── requirements.txt
├── runtime.txt
└── README.md
```

---

# 🚀 Future Improvements

Possible extensions for the project:

• Machine learning price prediction model  
• Automated data pipeline  
• Geospatial housing price visualisations  
• Docker deployment  
• Power BI / Tableau dashboard version  
• Real-time housing market data integration  

---

# 👤 Author

**Prem Nadh Gajula**

Aspiring **Data Scientist | Machine Learning Engineer | Backend Developer**

Interested in:

• Data Analytics  
• Machine Learning  
• Data-driven systems  

GitHub:  
https://github.com/premnadh

---

If you found this project useful, consider ⭐ starring the repository!