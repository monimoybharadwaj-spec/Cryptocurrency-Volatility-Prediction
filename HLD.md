# High-Level Design (HLD)

## 1. System Overview
This system predicts short-term cryptocurrency price volatility using a supervised machine learning model trained on historical market data.  
It is designed as a modular pipeline that supports data processing, feature engineering, model training, and real-time deployment.

The final model is exposed through a web-based user interface using Streamlit for live inference.

---

## 2. System Architecture

The system consists of four primary layers:

1. Data Layer – Ingests historical cryptocurrency market data  
2. Feature Engineering Layer – Transforms raw data into volatility-related indicators  
3. Modeling Layer – Trains, validates, and optimizes machine learning models  
4. Deployment Layer – Serves predictions through a Streamlit web application  

---

## 3. High-Level Workflow

```text
Historical Crypto Market Data (CSV)
        ↓
Data Cleaning & Validation
        ↓
Feature Engineering
(Returns, Volatility, ATR, Bollinger Bands, Liquidity Ratios)
        ↓
Time-Series Train/Test Split
        ↓
Model Training & Cross-Validation
        ↓
Hyperparameter Optimization
        ↓
Final Model Selection
        ↓
Model Serialization (Joblib)
        ↓
Model Hosting (GitHub Releases)
        ↓
Streamlit Web Application
        ↓
Live Volatility Prediction
```

## 4. Design Goals

The system was designed with the following objectives:

- **Time-Series Integrity**  
  Preserve chronological ordering to prevent data leakage and forward-looking bias.

- **Deployment Readiness**  
  Enable cloud-based deployment and real-time inference via a web application.

- **Reproducibility**  
  Ensure consistent preprocessing, feature engineering, and inference pipelines.

- **Scalability**  
  Allow the model to be retrained or replaced without changing the user interface.

- **Performance and Accuracy**  
  Use ensemble learning to capture non-linear relationships and improve prediction accuracy.

- **Usability**  
  Provide a simple and intuitive interface for users to generate volatility predictions.

---

## 5. Deployment Strategy

Due to GitHub file size constraints, the trained model is stored in **GitHub Releases** and dynamically downloaded by the Streamlit application at runtime.  
This allows large models to be deployed without bloating the source repository while keeping the system lightweight and reproducible.

The Streamlit Cloud environment automatically loads the model and exposes a real-time prediction interface to users.

---

## 6. Output

The system outputs **real-time cryptocurrency volatility predictions** based on user-provided technical indicators through the Streamlit web application.