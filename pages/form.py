
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

MODEL_PATH = "creditwise_pipeline.joblib"

st.set_page_config(
    page_title="LoanSense AI",
    layout="centered"
)

# ── FORM VERSION COUNTER (reset trick) ─────────────────────
if "form_version" not in st.session_state:
    st.session_state["form_version"] = 0
if "prediction_result" not in st.session_state:
    st.session_state["prediction_result"] = None

def reset_form():
    st.session_state["form_version"] += 1
    st.session_state["prediction_result"] = None

v = st.session_state["form_version"]

# ── TOP NAVBAR ──────────────────────────────────────────────
col1, col2 = st.columns([6, 1])

with col1:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:10px;">
        <div style="
            width:36px;height:36px;border-radius:10px;
            background:linear-gradient(135deg,#22C55E,#34D399);
            display:flex;align-items:center;justify-content:center;
            font-weight:800;color:#021F1A;font-size:18px;">
            ₹
        </div>
        <span style="font-weight:700;font-size:16px;color:#D1FAE5;">
            LoanSense AI
        </span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

st.divider()

# ── STYLING ─────────────────────────────────────────────────
st.markdown("""
<style>

/* PAGE BACKGROUND */
.stApp {
    background: radial-gradient(circle at 20% 20%, #0F6B5C 0%, #063D33 40%, #021F1A 100%);
}

/* FORM CONTAINER */
div[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.05);
    padding: 30px;
    border-radius: 16px;
    border: 1px solid rgba(52, 211, 153, 0.2);
    backdrop-filter: blur(10px);
}

/* LABELS */
div[data-testid="stWidgetLabel"] > label {
    font-size: 15px !important;
    font-weight: 600 !important;
    color: #D1FAE5 !important;
}

/* WHITE BACKGROUND FOR NUMBER INPUTS */
div[data-baseweb="input"] {
    background-color: #ffffff !important;
    border-radius: 8px !important;
}
div[data-baseweb="input"] input {
    background-color: #ffffff !important;
    color: #000000 !important;
    padding: 8px !important;
}
div[data-testid="stNumberInput"] > div {
    background-color: #ffffff !important;
    border-radius: 8px !important;
}
div[data-testid="stNumberInput"] button {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-left: 1px solid #e0e0e0 !important;
}

/* WHITE BACKGROUND FOR DROPDOWNS */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 8px !important;
}

/* HEADINGS */
h3 { color: #FFFFFF !important; }
p  { color: #A7F3D0 !important; }

/* HOME NAVBAR BUTTON */
div[data-testid="stButton"] > button {
    background: rgba(255, 255, 255, 0.05) !important;
    color: #D1FAE5 !important;
    border: 1px solid rgba(52, 211, 153, 0.4) !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}
div[data-testid="stButton"] > button:hover {
    background: rgba(52, 211, 153, 0.1) !important;
    color: #34D399 !important;
    border-color: #34D399 !important;
}

/* ── ALL FORM SUBMIT BUTTONS BASE ── */
div[data-testid="stFormSubmitButton"] > button {
    height: 48px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    width: 100% !important;
    border-radius: 10px !important;
    transition: all 0.2s ease !important;
}

/* ── PREDICT BUTTON — target by its text content via attribute ── */
div[data-testid="stFormSubmitButton"] > button[data-testid="baseButton-secondaryFormSubmit"]:first-child,
div[data-testid="stFormSubmitButton"] > button {
    background: rgba(52, 211, 153, 0.12) !important;
    color: #34D399 !important;
    border: 2px solid #34D399 !important;
}

/* Override specifically for the Predict button column */
div[data-testid="column"]:first-child div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(90deg, #22C55E, #34D399) !important;
    color: #021F1A !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(34,197,94,0.35) !important;
}
div[data-testid="column"]:first-child div[data-testid="stFormSubmitButton"] > button:hover {
    background: linear-gradient(90deg, #16a34a, #22c55e) !important;
    color: #ffffff !important;
    box-shadow: 0 6px 20px rgba(34,197,94,0.5) !important;
}

/* ── RESET BUTTON — second column ── */
div[data-testid="column"]:last-child div[data-testid="stFormSubmitButton"] > button {
    background: rgba(52, 211, 153, 0.1) !important;
    color: #34D399 !important;
    border: 2px solid #34D399 !important;
}
div[data-testid="column"]:last-child div[data-testid="stFormSubmitButton"] > button:hover {
    background: rgba(52, 211, 153, 0.25) !important;
    color: #ffffff !important;
    border-color: #86EFAC !important;
}

</style>
""", unsafe_allow_html=True)

# Subtitle
st.markdown(
    "<p style='text-align:center;'>Enter applicant details to predict whether the loan will be <b>Approved</b> or <b>Rejected</b>.</p>",
    unsafe_allow_html=True
)

# ── LOAD MODEL ──────────────────────────────────────────────
if not Path(MODEL_PATH).exists():
    st.error(
        f"Model file not found: {MODEL_PATH}\n\n"
        "Run training first:\n"
        "1) python train.py\n"
        "2) Then run: streamlit run app.py"
    )
    st.stop()

model = joblib.load(MODEL_PATH)

# ── OPTION LISTS ────────────────────────────────────────────
LOAN_TERMS       = [12, 24, 36, 48, 60, 72, 84]
LOAN_PURPOSES    = ["Home", "Education", "Personal", "Business", "Car"]
PROPERTY_AREAS   = ["Urban", "Semiurban", "Rural"]
EMP_STATUSES     = ["Salaried", "Self-employed", "Contract", "Unemployed"]
MARITAL_STATUSES = ["Single", "Married"]
EDU_LEVELS       = ["Graduate", "Not Graduate"]
GENDERS          = ["Male", "Female", "Other"]
EMPLOYER_CATS    = ["Government", "Private", "Business", "Unemployed", "MNC"]

# ── FORM ────────────────────────────────────────────────────
with st.form(f"loan_form_{v}"):
    st.subheader("Applicant Information")

    applicant_income = st.number_input(
        "Applicant Income (monthly)", min_value=0.0, step=500.0, value=0.0,
        key=f"applicant_income_{v}"
    )
    age = st.number_input(
        "Age", min_value=18, max_value=100, step=1, value=18,
        key=f"age_{v}"
    )
    dependents = st.number_input(
        "Dependents", min_value=0, max_value=10, step=1, value=0,
        key=f"dependents_{v}"
    )
    credit_score = st.number_input(
        "Credit Score", min_value=300, max_value=900, value=720,
        key=f"credit_score_{v}"
    )
    existing_loans = st.number_input(
        "Existing Loans", min_value=0, max_value=50, value=0,
        key=f"existing_loans_{v}"
    )
    coapplicant_income = st.number_input(
        "Coapplicant Income (monthly)", min_value=0.0, step=500.0, value=0.0,
        key=f"coapplicant_income_{v}"
    )
    savings = st.number_input(
        "Savings", min_value=0.0, step=1000.0, value=0.0,
        key=f"savings_{v}"
    )
    collateral_value = st.number_input(
        "Collateral Value", min_value=0.0, step=1000.0, value=0.0,
        key=f"collateral_value_{v}"
    )
    dti_ratio = st.number_input(
        "DTI Ratio (0.0 to 1.0)", min_value=0.0, max_value=1.0, step=0.01, value=0.0,
        key=f"dti_ratio_{v}"
    )

    st.subheader("Loan Details")

    loan_amount = st.number_input(
        "Loan Amount", min_value=0.0, step=5000.0, value=0.0,
        key=f"loan_amount_{v}"
    )
    loan_term = st.selectbox(
        "Loan Term (months)", LOAN_TERMS, index=0,
        key=f"loan_term_{v}"
    )
    loan_purpose = st.selectbox(
        "Loan Purpose", LOAN_PURPOSES, index=0,
        key=f"loan_purpose_{v}"
    )
    property_area = st.selectbox(
        "Property Area", PROPERTY_AREAS, index=0,
        key=f"property_area_{v}"
    )
    employment_status = st.selectbox(
        "Employment Status", EMP_STATUSES, index=0,
        key=f"employment_status_{v}"
    )
    marital_status = st.selectbox(
        "Marital Status", MARITAL_STATUSES, index=0,
        key=f"marital_status_{v}"
    )
    education_level = st.selectbox(
        "Education Level", EDU_LEVELS, index=0,
        key=f"education_level_{v}"
    )
    gender = st.selectbox(
        "Gender", GENDERS, index=0,
        key=f"gender_{v}"
    )
    employer_category = st.selectbox(
        "Employer Category", EMPLOYER_CATS, index=0,
        key=f"employer_category_{v}"
    )

    # ── BUTTONS SIDE BY SIDE ────────────────────────────────
    col_submit, col_reset = st.columns([1, 1])
    with col_submit:
        submitted = st.form_submit_button("✅  Predict", use_container_width=True)
    with col_reset:
        reset_clicked = st.form_submit_button("🔄  Reset Form", use_container_width=True)

# ── HANDLE RESET ────────────────────────────────────────────
if reset_clicked:
    reset_form()
    st.rerun()

# ── PREDICTION ──────────────────────────────────────────────
if submitted:
    st.session_state["prediction_result"] = None

    input_df = pd.DataFrame([{
        "Applicant_Income":   applicant_income,
        "Coapplicant_Income": coapplicant_income,
        "Employment_Status":  employment_status,
        "Age":                age,
        "Marital_Status":     marital_status,
        "Dependents":         dependents,
        "Credit_Score":       credit_score,
        "Existing_Loans":     existing_loans,
        "DTI_Ratio":          dti_ratio,
        "Savings":            savings,
        "Collateral_Value":   collateral_value,
        "Loan_Amount":        loan_amount,
        "Loan_Term":          loan_term,
        "Loan_Purpose":       loan_purpose,
        "Property_Area":      property_area,
        "Education_Level":    education_level,
        "Gender":             gender,
        "Employer_Category":  employer_category
    }])

    pred = model.predict(input_df)[0]

    proba_text = ""
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(input_df)[0]
        pred_idx = list(model.classes_).index(pred) if hasattr(model, "classes_") else None
        if pred_idx is not None:
            proba_text = f" (confidence: {probs[pred_idx]:.2f})"

    approved = (pred == 1) or (str(pred).lower() in ["yes", "approved", "true"])
    st.session_state["prediction_result"] = (approved, proba_text, input_df)

# ── SHOW RESULT ─────────────────────────────────────────────
if st.session_state.get("prediction_result"):
    approved, proba_text, input_df = st.session_state["prediction_result"]
    if approved:
        st.success(f"✅ Prediction: APPROVED{proba_text}")
    else:
        st.error(f"❌ Prediction: REJECTED{proba_text}")

    with st.expander("Show submitted input"):
        st.dataframe(input_df, use_container_width=True)