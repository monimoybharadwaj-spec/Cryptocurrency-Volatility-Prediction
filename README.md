
# Cryptocurrency Volatility Prediction  

---

## Problem Statement
Cryptocurrency markets are highly volatile, making risk management, trading strategies, and portfolio allocation extremely difficult. This project builds a machine learning system to predict short-term cryptocurrency price volatility using historical market data and technical indicators. Instead of predicting price direction, this system predicts how unstable the price will be in the near future.

---

## What is Volatility Prediction?
Volatility measures how much an asset’s price fluctuates over time. High volatility means large and unpredictable price movements, while low volatility indicates more stable prices.

In this project, volatility is modeled as the rolling standard deviation of log returns and predicted using technical and liquidity-based indicators derived from historical market data. The system does not try to predict whether the price will go up or down — it predicts how unstable the market will be, which is critical for risk management, position sizing, options pricing, portfolio allocation, and algorithmic trading.

---

## End-to-End Machine Learning Workflow

---

## Live Demo
Try the live application here:  
https://cryptocurrency-volatility-prediction-monimoy.streamlit.app

---

## Dataset
The dataset used in this project is included directly in this repository as `dataset.csv`.

It contains historical cryptocurrency market data with common fields such as:
- Open, High, Low, Close prices  
- Volume  
- Market capitalization  
- Timestamps (date/time)

This data is used to compute:
- Log returns  
- Rolling volatility  
- Liquidity metrics  
- Other engineered features used for modeling

The dataset can be accessed here:  
https://github.com/monimoybharadwaj-spec/Cryptocurrency-Volatility-Prediction/blob/main/dataset.csv

---

## Feature Engineering
The following technical and liquidity indicators were engineered:

- Log returns  
- Rolling volatility  
- Average True Range (ATR)  
- Bollinger Band width  
- Moving averages  
- Volume to market-cap ratio  

These features capture both price dynamics and market liquidity effects on volatility.

---

## Models Evaluated
Multiple regression models were trained and compared:

- Linear Regression  
- K-Nearest Neighbors  
- Support Vector Regressor  
- Decision Tree Regressor  
- Gradient Boosting Regressor  
- Random Forest Regressor (Final Model)  

Time-series aware train-test splitting was used to prevent data leakage.

---

## Final Model Performance (Random Forest)

| Metric | Value |
|------|-------|
| RMSE | ≈ 0.015 |
| MAE  | ≈ 0.009 |
| R²   | ≈ 0.86 |

---

## Deployment Architecture

The application is deployed using Streamlit and follows a clean production-style setup:

| Component | Location |
|--------|--------|
| Source code | GitHub repository |
| Trained model | GitHub Releases |
| Inference | Streamlit Cloud |
| User Interface | Web browser |

Due to GitHub file size limits, the trained model (rf_volatility_model.pkl) is stored in GitHub Releases and automatically downloaded by the Streamlit application at runtime.

Model download URL used by the app:
https://github.com/monimoybharadwaj-spec/Cryptocurrency-Volatility-Prediction/releases/download/V1/rf_volatility_model.pkl

---

## How to Run Locally

pip install -r requirements.txt  
streamlit run app.py  

The application will automatically download the trained model if it is not present.

---

## Project Highlights
- Real-world financial volatility modeling  
- Time-series aware validation  
- Feature-rich ML pipeline  
- Large model handled using GitHub Releases  
- Fully deployed interactive web application  

---

## Author
Monimoy Bharadwaj  
Cryptocurrency Volatility Prediction — End-to-End Machine Learning Project