

import streamlit as st
import joblib
import numpy as np
from xgboost import  XGBClassifier
# Loading our saved model

import os
best_xgb = joblib.load(os.path.join(os.path.dirname(__file__), "aura.pk1"))

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📊")

st.title("📊Customer Churn Prediction")
st.write("Enter customer details below to predict churn probability")

# Here we will add our top features by which our model has been trained for finding best churn probability
contract = st.selectbox("Contract-Type",["Month-to-month", "One year","Two year"])
Online_Security = st.selectbox("Online Security",["Yes", "No"])
payment_method = st.selectbox("Payment Menthod",["Electronic check", "Credit card(automatic)","Mailed check","Bank transfer(automatic)"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fibre optic", "No"])
tech_support =  st.selectbox("Tech Support", ["Yes","No"])

#
contract_month = 1 if contract == "Month-to-month" else 0 
Online_Security_no = 1 if Online_Security == "No" else 0
payment_electronic = 1 if payment_method == "Electronic check" else 0
internet_fibre = 1 if internet_service == "Fibre optic" else 0 
tech_support_no = 1 if tech_support == "No" else 0 

features = np.zeros((1,40))

features[0, 12] = contract_month
features[0, 22] = Online_Security_no
features[0,17] = payment_electronic
features[0, 10] = internet_fibre
features[0, 31] = tech_support_no


if st.button("Predict churn"):
    prediction = best_xgb.predict(features)[0]
    probability = best_xgb.predict_proba(features)[0][1]

    if prediction ==1:
        st.error(f"⚠️ This customer is likely to churn! (probability: {probability:.2f})")
    else:
        st.success(f"✅This customer is not likely to churn. (probability: {probability:.2f})")

