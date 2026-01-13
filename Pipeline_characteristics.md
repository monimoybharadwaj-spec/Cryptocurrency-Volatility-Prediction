# Pipeline Architecture

Raw Cryptocurrency Market Data (CSV)
        ↓
Data Cleaning & Validation
        ↓
Exploratory Data Analysis (EDA)
        ↓
Feature Engineering (Returns, Volatility, ATR, Bollinger Bands, Liquidity Ratios)
        ↓
Rolling Window Alignment & NaN Handling
        ↓
Feature–Target Matrix Construction
        ↓
Time-Series Train–Test Split
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
Streamlit Cloud Inference API
        ↓
Live Web Application
