# 🛍️ RetailPulse AI
### AI-Powered Retail Analytics Platform for Customer Intelligence, Churn Prediction, Demand Forecasting & Inventory Optimization

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green)
![Prophet](https://img.shields.io/badge/Forecasting-Prophet-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

# 📌 Project Overview

RetailPulse AI is an end-to-end Retail Analytics platform developed to help businesses make data-driven decisions.

The project combines Customer Segmentation, Churn Prediction, Demand Forecasting and Inventory Optimization into one intelligent dashboard.

Instead of only analyzing historical sales, the platform identifies valuable customers, predicts customers likely to churn, forecasts future sales using Facebook Prophet and recommends inventory decisions to reduce stock shortages and overstocking.

The project has been deployed as an interactive Streamlit dashboard.

---

# 🎯 Business Problem

Retail companies often struggle with:

- Identifying high-value customers.
- Detecting customers likely to churn.
- Predicting future sales demand.
- Maintaining optimal inventory.
- Making business decisions using historical sales data.

RetailPulse solves all these problems in one integrated analytics platform.

---

# 🚀 Features

## 📊 Customer Segmentation

Implemented RFM (Recency, Frequency, Monetary) Analysis.

Performed:

- Data Cleaning
- Outlier Removal
- Feature Scaling
- KMeans Clustering
- Customer Segmentation

Customer Groups:

- 🏆 Champions
- ❤️ Loyal Customers
- 🌟 Potential Loyalists
- 🆕 New Customers
- ⚠️ At Risk
- ❌ Lost Customers

---

## 🤖 Churn Prediction

Customers belonging to the "At Risk" segment were treated as churn-prone customers.

Built a XGBoost for predicting churn probability.

Model Evaluation:

- ROC AUC ≈ 0.99
- Accuracy ≈ 99%
- Precision@Top20 implemented precision_top_20 = 0.43

---

## 📈 Demand Forecasting

Used Facebook Prophet to forecast sales for the next 30 days.

Features:

- Daily Sales Aggregation
- Trend Analysis
- Weekly Seasonality
- Yearly Seasonality
- Future Sales Prediction
- Forecast Components

Model Performance:

MAPE ≈ 7.4%

---

## 📦 Inventory Optimization

Using forecasted sales, calculated:

- Daily Demand
- Reorder Point
- Safety Stock
- Reorder Quantity

Goal:

Reduce

- Overstock,
- Understock by 25 - 40 %

while maintaining inventory availability.

---

# 🛠️ Tech Stack

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Prophet
- Joblib
- Streamlit

---

# 📂 Project Workflow

```
Raw Retail Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
RFM Analysis
        │
        ▼
Customer Segmentation
        │
        ▼
Churn Prediction
        │
        ▼
Demand Forecasting
        │
        ▼
Inventory Optimization
        │
        ▼
Streamlit Dashboard
```

---

# 📊 Machine Learning Models

| Task | Algorithm |
|-------|-----------|
| Customer Segmentation | KMeans |
| Churn Prediction | XGBoost |
| Demand Forecasting | Prophet |

---

# 📁 Project Structure

```
RetailPulse/
│
├── dashboard/
│     ├── app.py
│     ├── churn_model.pkl
│     ├── Future_sales_forecast.csv
│     └── inventory_optimization.csv
│
├── notebooks/
│     ├── CustomerSegmentation.ipynb
│     ├── ChurnPrediction.ipynb
│     ├── DemandForecasting.ipynb
│     └── InventoryOptimization.ipynb
│
├── dataset/
│
│
└── README.md
```

---

# 📷 Dashboard Preview

## Home Page

<img width="1920" height="1541" alt="image" src="https://github.com/user-attachments/assets/99eb6a38-4b78-4075-89c5-281254ac5e3a" />


---

## Customer Segmentation

<img width="1920" height="2170" alt="image" src="https://github.com/user-attachments/assets/36182bfd-83a3-433c-8a45-d5dbbecf8136" />



---

## Churn Prediction

<img width="1920" height="1817" alt="image" src="https://github.com/user-attachments/assets/6d3c2c41-7549-4e1e-9750-83c9d7cc974f" />

---

## Demand Forecasting

<img width="1920" height="2106" alt="image" src="https://github.com/user-attachments/assets/3b5abc8a-fb70-47a7-8e71-c4360a6fdd23" />


---

## Inventory Optimization

<img width="1920" height="2121" alt="image" src="https://github.com/user-attachments/assets/dd7c47db-84e9-4cc7-a520-515ee67efcc7" />


---

# 📈 Key Insights

✔ Identified high-value customer groups.

✔ Predicted customers likely to churn.

✔ Forecasted next 30 days sales.

✔ Calculated optimal inventory levels.

✔ Built an end-to-end interactive retail analytics dashboard.

---

# ▶️ Installation

Clone Repository

```bash
git clone https://github.com/yourusername/RetailPulse.git
```

Go inside folder

```bash
cd RetailPulse
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 📌 Future Improvements:-

- Random Forest Churn Model.
- Real-Time Data Integration.
- Product Level Demand Forecasting.
- Cloud Deployment.
- SQL Database Integration.

---

# 👨‍💻 Author

**Shivam Dwivedi**

B.Tech Computer Science Engineering

Passionate about

- Data Analytics
- Machine Learning
- Artificial Intelligence
- Business Intelligence

LinkedIn:
https://www.linkedin.com/in/shivam-dwivedi-27661a395/?skipRedirect=true

GitHub:
https://github.com/shivamdwivedicse

---

⭐ If you found this project useful, consider giving it a star.
