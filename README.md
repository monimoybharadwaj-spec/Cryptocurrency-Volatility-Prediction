# Cryptocurrency Volatility Prediction using Machine Learning

## Project Overview
This project builds and deploys a machine learning system to predict short-term cryptocurrency price volatility.  
Volatility is modeled as the rolling standard deviation of log returns and predicted using technical and liquidity-based indicators derived from historical market data.

The project follows a complete end-to-end data science lifecycle including:
- Data preprocessing and cleaning  
- Exploratory data analysis  
- Feature engineering  
- Model training and comparison  
- Hyperparameter tuning  
- Model deployment using Streamlit  

---

## Live Demo
Try the live application here:  
https://cryptocurrency-volatility-prediction-monimoy.streamlit.app

---

## Dataset
- Source: Historical cryptocurrency market data  
- Features: Open, High, Low, Close prices, Trading Volume, Market Capitalization  
- Multiple cryptocurrencies included  
- Time-series structure preserved throughout the workflow  

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