# Cryptocurrency Volatility Prediction using Machine Learning

## Project Overview
This project focuses on predicting short-term cryptocurrency price volatility using
machine learning techniques. Volatility is modeled as the rolling standard deviation
of log returns and predicted using engineered technical and liquidity-based indicators.

The project follows a complete data science lifecycle including data preprocessing,
exploratory data analysis, feature engineering, model comparison, hyperparameter tuning,
and deployment using Streamlit.

---

## Dataset
- Source: Historical cryptocurrency market data
- Features include: Open, High, Low, Close prices, Volume, Market Capitalization
- Multiple cryptocurrencies are included
- Time-series structure preserved throughout the workflow

---

## Key Features
- Log return–based volatility modeling
- Technical indicators (ATR, Bollinger Bands, Moving Average)
- Comparison of multiple regression models
- Time-series aware validation
- Random Forest selected as final model
- Interactive Streamlit deployment

---

## Models Used
- Linear Regression
- K-Nearest Neighbors
- Support Vector Regressor
- Decision Tree Regressor
- Random Forest Regressor (Final Model)
- Gradient Boosting Regressor

---

## Final Model Performance (Random Forest)
- RMSE ≈ 0.015
- MAE ≈ 0.009
- R² ≈ 0.86

---

## Deployment
The trained model is deployed using Streamlit, allowing users to input technical
indicators and receive real-time volatility predictions.

To run locally:
```bash
streamlit run app.py

---

## Deployment Note

Due to GitHub file size limitations, the trained model file is not stored
in this repository. The Streamlit application demonstrates the deployment
pipeline and user interface. The complete project, including the trained
model, is provided separately as a ZIP file.