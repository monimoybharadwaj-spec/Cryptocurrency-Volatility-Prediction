# Cryptocurrency Volatility Prediction Using Machine Learning

## 1. Introduction
Cryptocurrency markets are highly volatile due to speculative trading, liquidity
variation, and rapid market sentiment changes. Accurate volatility estimation is
important for risk management, trading strategies, and financial analysis.
This project aims to predict short-term cryptocurrency volatility using historical
market data and machine learning techniques.

---

## 2. Objective
The primary objective of this project is to:
- Model short-term price volatility using historical cryptocurrency data
- Engineer meaningful technical and liquidity-based features
- Compare multiple regression models
- Select and optimize the best-performing model
- Deploy the final model using a Streamlit web application

---

## 3. Dataset Description
The dataset consists of historical cryptocurrency market data with the following fields:
- Open, High, Low, Close prices
- Trading Volume
- Market Capitalization
- Date and Cryptocurrency identifier

Multiple cryptocurrencies are included, and the time-series structure of the data
is preserved throughout the analysis.

---

## 4. Exploratory Data Analysis (EDA)
Key observations from EDA include:
- Strong correlations among Open, High, Low, and Close prices
- Price trends exhibit significant temporal variation across assets
- Trading volume and market capitalization show moderate association with prices
- Volatility varies substantially across time and cryptocurrencies

These insights motivated the use of derived features rather than raw price values.

---

## 5. Feature Engineering
The following features were engineered:

- **Log Returns:** Stabilize variance and capture relative price changes  
- **Rolling Volatility (Target Variable):** 14-day rolling standard deviation of log returns  
- **Volume-to-MarketCap Ratio:** Liquidity indicator  
- **Moving Average (14-day):** Captures short-term trend  
- **Bollinger Band Width:** Measures price dispersion  
- **Average True Range (ATR-14):** Captures intraday price range volatility  

All rolling features were computed separately for each cryptocurrency to avoid
cross-asset data leakage.

---

## 6. Model Selection and Training
The dataset was split into training and test sets using a chronological split
(shuffle disabled) to preserve temporal order.

The following regression models were evaluated:
- Linear Regression
- K-Nearest Neighbors
- Support Vector Regressor
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

Scale-sensitive models were trained using standardized features, while tree-based
models were trained on unscaled data.

---

## 7. Model Evaluation
Models were evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Performance Summary:
- **Random Forest Regressor** achieved the best overall performance  
- Ensemble tree-based models outperformed linear and distance-based models  
- Results indicate non-linear relationships between engineered indicators and volatility  

Final Random Forest performance on the test set:
- RMSE ≈ 0.015
- MAE ≈ 0.009
- R² ≈ 0.86

---

## 8. Hyperparameter Optimization
Random Forest hyperparameters were optimized using `RandomizedSearchCV` with
`TimeSeriesSplit` to maintain temporal integrity.
This resulted in a modest but consistent improvement in predictive performance.

---

## 9. Deployment
After evaluation, the final Random Forest model was retrained on the complete dataset
using optimal hyperparameters for deployment purposes.
The model was deployed using a Streamlit web application that allows users to input
technical indicators and receive predicted volatility in real time.

---

## 10. Conclusion
This project demonstrates an end-to-end machine learning workflow for cryptocurrency
volatility prediction, including time-series–aware validation and deployment.
Feature engineering and ensemble learning were key contributors to model performance.
The deployed application provides an accessible interface for real-time inference.