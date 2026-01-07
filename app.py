import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and features
with open("rf_volatility_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model_features.pkl", "rb") as f:
    feature_names = pickle.load(f)

st.set_page_config(page_title="Crypto Volatility Predictor", layout="centered")

st.title("Cryptocurrency Volatility Prediction")
st.write("Predict rolling volatility using technical indicators.")

st.subheader("Input Features")

# User inputs
volume_marketcap_ratio = st.number_input(
    "Volume / Market Cap Ratio", min_value=0.0, value=0.01
)

ma_close = st.number_input(
    "14-day Moving Average of Close Price", min_value=0.0, value=1000.0
)

bollinger_width = st.number_input(
    "Bollinger Band Width", min_value=0.0, value=0.05
)

atr_14 = st.number_input(
    "ATR (14-day)", min_value=0.0, value=10.0
)

# Prediction
if st.button("Predict Volatility"):
    input_data = pd.DataFrame([[
        volume_marketcap_ratio,
        ma_close,
        bollinger_width,
        atr_14
    ]], columns=feature_names)

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Volatility: {prediction:.5f}")