# High-Level Design (HLD) Document

## 1. System Overview
The system predicts cryptocurrency volatility using a supervised machine learning
model trained on historical market data. The system consists of data ingestion,
feature engineering, model training, evaluation, and deployment layers.

---

## 2. Architecture Overview

**Components**
1. Data Layer  
2. Feature Engineering Layer  
3. Model Training & Evaluation Layer  
4. Deployment Layer (Streamlit)

---

## 3. High-Level Architecture Flow

Raw Market Data
↓
Data Preprocessing
↓
Feature Engineering
↓
Model Training & Validation
↓
Hyperparameter Optimization
↓
Final Model
↓
Streamlit Application

---

## 4. Design Goals
- Preserve temporal ordering (time-series safety)
- Avoid data leakage
- Ensure model interpretability
- Enable real-time inference via UI