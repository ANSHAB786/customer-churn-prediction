import streamlit as st
import joblib
import numpy as np
import os

# Page config
st.set_page_config(page_title="Customer Churn Predictor", page_icon="📉", layout="centered")

# Load model
best_xgb = joblib.load(os.path.join(os.path.dirname(__file__), "aura.pk1"))
# Header
st.title("📉 Customer Churn Prediction")
st.markdown("#### Predict whether a customer is likely to leave based on their profile")
st.markdown("---")

# Input section
st.subheader("👤 Customer Details")

col1, col2 = st.columns(2)

with col1:
    contract = st.radio("📋 Contract Type", ["Month-to-month", "One year", "Two year"])
    Online_Security = st.radio("🔒 Online Security", ["Yes", "No"])
    internet_service = st.radio("🌐 Internet Service", ["DSL", "Fibre optic", "No"])

with col2:
    payment_method = st.radio("💳 Payment Method", ["Electronic check", "Credit card(automatic)", "Mailed check", "Bank transfer(automatic)"])
    tech_support = st.radio("🛠️ Tech Support", ["Yes", "No"])
    monthly_charges = st.slider("💰 Monthly Charges ($)", min_value=0, max_value=150, value=65)
    tenure = st.slider("📅 Tenure (months)", min_value=0, max_value=72, value=12)

st.markdown("---")
# Feature engineering
contract_month = 1 if contract == "Month-to-month" else 0
contract_one_year = 1 if contract == "One year" else 0
Online_Security_no = 1 if Online_Security == "No" else 0
payment_electronic = 1 if payment_method == "Electronic check" else 0
internet_fibre = 1 if internet_service == "Fibre optic" else 0
tech_support_no = 1 if tech_support == "No" else 0

features = np.zeros((1, 40))
features[0, 4] = tenure
features[0, 7] = monthly_charges
features[0, 12] = contract_month
features[0, 13] = contract_one_year
features[0, 17] = payment_electronic
features[0, 22] = Online_Security_no
features[0, 31] = tech_support_no
features[0, 10] = internet_fibre

# Feature engineering
 #contract_month = 1 if contract == "Month-to-month" else 0
#Online_Security_no = 1 if Online_Security == "No" else 0
#payment_electronic = 1 if payment_method == "Electronic check" else 0
#internet_fibre = 1 if internet_service == "Fibre optic" else 0
#tech_support_no = 1 if tech_support == "No" else 0
 ###
#features = np.zeros((1, 40))
#features[0, 4] = tenure
#features[0, 7] = monthly_charges
#features[0, 12] = contract_month
#features[0, 22] = Online_Security_no
#features[0, 17] = payment_electronic
#features[0, 10] = internet_fibre
#features[0, 31] = tech_support_no
 ###
# Predict button
if st.button("🔍 Predict Churn", use_container_width=True):
    prediction = best_xgb.predict(features)[0]
    probability = float(best_xgb.predict_proba(features)[0][1])
    churn_pct = round(probability * 100, 1)

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    # Risk level
    if churn_pct >= 70:
        risk = "High Risk 🔴"
        color = "error"
    elif churn_pct >= 40:
        risk = "Mid Risk 🟡"
        color = "warning"
    else:
        risk = "Low Risk 🟢"
        color = "success"

    # Metrics row
    col1, col2, col3 = st.columns(3)
    col1.metric("Churn Probability", f"{churn_pct}%")
    col2.metric("Risk Level", risk)
    col3.metric("Lifetime Value at Risk", f"~${round(churn_pct/100 * 2101):,}")
    # Result message
    if probability >= 0.37:
        st.error(f"⚠️ This customer is **likely to churn** with {churn_pct}% probability!")
        st.markdown("### 💡 Recommended Actions:")
        if contract_month:
            st.markdown("- 📋 Offer a **discounted annual contract** to lock in the customer")
        if Online_Security_no:
            st.markdown("- 🔒 Provide **free Online Security** add-on for 3 months")
        if payment_electronic:
            st.markdown("- 💳 Incentivize switch to **automatic payment** with a discount")
        if internet_fibre:
            st.markdown("- 🌐 Investigate **Fiber Optic service quality** issues")
        if tech_support_no:
            st.markdown("- 🛠️ Offer **free Tech Support** trial for 1 month")
        if monthly_charges > 92:
            st.markdown("- 💰 Monthly charges are **above $92** — consider a loyalty discount")
    else:
        st.success(f"✅ This customer is **not likely to churn** with only {churn_pct}% probability!")
        st.markdown("### 💡 Retention Tips:")
    
    if contract_month == 0:
        st.markdown("- 📋 Customer is on a **long-term contract** — great for retention!")
    if Online_Security_no == 0:
        st.markdown("- 🔒 Customer has **Online Security** — keep offering security features")
    if payment_electronic == 0:
        st.markdown("- 💳 Customer uses **automatic payment** — low churn risk, reward them")
    if internet_fibre == 0:
        st.markdown("- 🌐 Customer uses **DSL** — stable and satisfied, send a loyalty reward")
    if tech_support_no == 0:
        st.markdown("- 🛠️ Customer has **Tech Support** — they feel supported, keep it up")
    if monthly_charges <= 92:
        st.markdown("- 💰 Monthly charges are **reasonable** — customer likely finds value")
    
    st.markdown("- 🌟 Send a **loyalty reward** to keep engagement high")
    st.markdown("- 📧 Check in with a **satisfaction survey**")

st.markdown("---")
st.caption("Built by Anshab Shaikh | Customer Churn Prediction System | XGBoost Model")