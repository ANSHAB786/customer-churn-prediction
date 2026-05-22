# 📉 Customer Churn Prediction System

A machine learning project that predicts customer churn for a telecom company,
quantifies business impact, and delivers real-time predictions via a deployed Streamlit web app.

---

## 🚀 Live Demo
👉 [Click here to try the app](your-streamlit-url-here)

---

## 📌 Problem Statement
A telecom company is losing customers silently. Each churned customer represents
~$2,101 in lost lifetime value. With 7,043 customers analyzed, the company was
losing approximately $3.93M/year due to churn.

---

## 🎯 Objective
- Predict which customers are likely to churn
- Identify key drivers of churn using SHAP
- Quantify business impact in dollar terms
- Deploy a real-time prediction app for business use

---

## 📂 Project Structure
```
customer-churn-prediction/
├── Notebook/
│   └── Customer_churn_Ai.ipynb   
├── data/                          
├── streamlit/
│   ├── app.py                     
│   └── aura.pk1                   
├── requirements.txt               
└── README.md                      
```

---

## 🔧 Tech Stack
| Category | Tools |
|---|---|
| Language | Python |
| ML Models | XGBoost, Logistic Regression, Random Forest, SVM, KNN |
| Imbalance Handling | SMOTE |
| Explainability | SHAP |
| Visualization | Matplotlib, Seaborn, Plotly |
| Deployment | Streamlit |
| Model Saving | Joblib |

---

## 📊 Key Results
| Metric | Score |
|---|---|
| Accuracy | 75% |
| Recall (Churn Class) | 73% |
| Threshold | 0.37 (optimized for recall) |

---

## 💡 Key Insights
- **Monthly Charges > $92** is the strongest churn signal
- **Month-to-month contracts** churn at significantly higher rates
- **Fiber Optic customers** churn more than DSL users
- **Customers without Online Security** are at higher risk

---

## 💰 Business Impact
- Company losing **~$3.93M/year** due to churn
- Each lost customer = **~$2,101 lifetime value**
- Model identifies **73% of churners** before they leave
- Recommended actions: promote annual contracts, incentivize auto-payment, improve Fiber Optic service

---

## ⚙️ How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/ANSHAB786/customer-churn-prediction.git
cd customer-churn-prediction
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Download dataset from Kaggle**
https://www.kaggle.com/datasets/blastchar/telco-customer-churn
Place it inside the `data/` folder

**4. Run the Streamlit app**
```bash
cd streamlit
streamlit run app.py
```

---

## 👤 Author
**Anshab Shaikh**
- 📧 shaikhanshab786@gmail.com
- 🔗 [LinkedIn](https://linkedin.com/in/anshab-shaikh)
- 🐙 [GitHub](https://github.com/ANSHAB786)