import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

MODEL_PATH = "creditwise_pipeline.joblib"

st.set_page_config(
    page_title="ML-Based Loan Approval Predictor",
    page_icon="💳",
    layout="centered"
)

st.title("💳 ML-Based Loan Approval Predictor")
st.write("Enter applicant details to predict whether the loan will be **Approved** or **Rejected**.")

# --- Load model ---
if not Path(MODEL_PATH).exists():
    st.error(
        f"Model file not found: {MODEL_PATH}\n\n"
        "Run training first:\n"
        "1) python train.py\n"
        "2) Then run: streamlit run app.py"
    )
    st.stop()

model = joblib.load(MODEL_PATH)

# --- Input form ---
with st.form("loan_form"):
    st.subheader("Applicant Information")

    col1, col2 = st.columns(2)
    with col1:
        applicant_income = st.number_input("Applicant Income (monthly)", min_value=0.0, value=30000.0, step=500.0)
        age = st.number_input("Age", min_value=18, max_value=100, value=28, step=1)
        dependents = st.number_input("Dependents", min_value=0, max_value=10, value=0, step=1)
        credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=720, step=1)
        existing_loans = st.number_input("Existing Loans", min_value=0, max_value=50, value=0, step=1)

    with col2:
        coapplicant_income = st.number_input("Coapplicant Income (monthly)", min_value=0.0, value=0.0, step=500.0)
        savings = st.number_input("Savings", min_value=0.0, value=50000.0, step=1000.0)
        collateral_value = st.number_input("Collateral Value", min_value=0.0, value=0.0, step=1000.0)
        dti_ratio = st.number_input("DTI Ratio (0.0 to 1.0)", min_value=0.0, max_value=1.0, value=0.25, step=0.01)

    st.subheader("Loan Details")

    col3, col4 = st.columns(2)
    with col3:
        loan_amount = st.number_input("Loan Amount", min_value=0.0, value=300000.0, step=5000.0)
        loan_term = st.selectbox("Loan Term (months)", [12, 24, 36, 48, 60, 72, 84], index=2)
        loan_purpose = st.selectbox("Loan Purpose", ["Home", "Education", "Personal", "Business", "Car"])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    with col4:
        employment_status = st.selectbox("Employment Status", ["Salaried", "Self-employed", "Contract", "Unemployed"])
        marital_status = st.selectbox("Marital Status", ["Single", "Married"])
        education_level = st.selectbox("Education Level", ["Graduate", "Not Graduate"])
        gender = st.selectbox("Gender", ["Male", "Female"])
        employer_category = st.selectbox("Employer Category", ["Government", "Private", "Business", "Unemployed", "MNC"])

    submitted = st.form_submit_button("Predict")

if submitted:
    # IMPORTANT: column names
    input_df = pd.DataFrame([{
        "Applicant_Income": applicant_income,
        "Coapplicant_Income": coapplicant_income,
        "Employment_Status": employment_status,
        "Age": age,
        "Marital_Status": marital_status,
        "Dependents": dependents,
        "Credit_Score": credit_score,
        "Existing_Loans": existing_loans,
        "DTI_Ratio": dti_ratio,
        "Savings": savings,
        "Collateral_Value": collateral_value,
        "Loan_Amount": loan_amount,
        "Loan_Term": loan_term,
        "Loan_Purpose": loan_purpose,
        "Property_Area": property_area,
        "Education_Level": education_level,
        "Gender": gender,
        "Employer_Category": employer_category
    }])

    pred = model.predict(input_df)[0]

    proba_text = ""
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(input_df)[0]
        # show probability of the predicted class
        pred_idx = list(model.classes_).index(pred) if hasattr(model, "classes_") else None
        if pred_idx is not None:
            proba_text = f" (confidence: {probs[pred_idx]:.2f})"

    # Handle both possible label types: 0/1 or "Yes"/"No"
    approved = (pred == 1) or (str(pred).strip().lower() in ["yes", "approved", "true"])

    if approved:
        st.success(f"Prediction: APPROVED{proba_text}")
    else:
        st.error(f"Prediction: REJECTED{proba_text}")

    with st.expander("Show submitted input"):
        st.dataframe(input_df, use_container_width=True)
