# 🏠 UK House Price Analysis & Dashboard

An end-to-end Data Analytics project analysing the UK housing market using
data cleaning, exploratory analysis, and an interactive Streamlit dashboard.

This project demonstrates a full real-world data workflow:
Data Collection → Cleaning → Analysis → Visualization → Deployment

---

## 🌐 Live Dashboard
👉 https://uk-house-price-analysis-dqzntjmkycmty2379wdnkp.streamlit.app/

---

## 🎯 Project Objective
Analyse UK housing market trends and build an interactive dashboard that helps
users explore:

• House price trends over time  
• Regional price differences  
• Property type comparisons  
• Key housing market insights  

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualisation | Plotly |
| Dashboard | Streamlit |
| Environment | Jupyter Notebook, VS Code |
| Version Control | Git & GitHub |

---

## 🔄 Project Workflow

### 1️⃣ Data Collection
UK housing dataset collected and prepared for analysis.

### 2️⃣ Data Cleaning & Processing
Performed using Pandas:
• Removed missing values  
• Converted date formats  
• Created yearly features  
• Aggregated regional statistics  
• Saved cleaned dataset for dashboard use  

Output file:
data/processed/cleaned_housing.csv

---

### 3️⃣ Exploratory Data Analysis (EDA)
Key questions answered:
• How have house prices changed over time?  
• Which regions are most expensive?  
• Which property types cost the most?  

EDA performed in Jupyter Notebook.

---

### 4️⃣ Dashboard Development (Streamlit)

Interactive dashboard includes:

• KPI Metrics  
  - Average UK House Price  
  - Highest Price Region  
  - Most Expensive Property Type  

• Interactive Filters  
  - Region filter  
  - Year filter  

• Visualisations  
  - House price trend over time  
  - Average price by region  
  - Average price by property type  

---

## 📊 Key Insights
• UK house prices show long-term upward trend  
• Significant regional price gap exists  
• Detached properties consistently most expensive  

---

## ▶️ Run Locally

Clone repository:
git clone https://github.com/premnadh/uk-house-price-analysis.git

Navigate into project:
cd uk-house-price-analysis

Install dependencies:
pip install -r requirements.txt

Run dashboard:
streamlit run dashboard/app.py

---

## 📂 Project Structure

uk-house-price-analysis/
│
├── dashboard/
│   └── app.py
├── data/
│   └── processed/
│       └── cleaned_housing.csv
├── notebooks/
│   └── eda.ipynb
├── requirements.txt
├── runtime.txt
└── README.md

---

## 🚀 Future Improvements
• Add machine learning price prediction model  
• Deploy using Docker / AWS / Render  
• Add Power BI dashboard version  
• Add automated data pipeline

---

## 👤 Author
PremNadh Gajula  
Aspiring Data Scientist / ML Engineer  
Open to Data & AI roles

If you like this project, please ⭐ the repository!