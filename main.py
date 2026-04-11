import streamlit as st
from Prediction_helper import predict

st.set_page_config(page_title="Loki Finance Dashboard", layout="wide")

# -------------------- CSS --------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

/* Title */
.title {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Output Cards */
.output-card {
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    background: rgba(255,255,255,0.02);
}

/* INPUT FIELD STROKE STYLE */
input, .stNumberInput input {
    background: transparent !important;
    border: 1px solid white !important;
    border-radius: 8px !important;
    color: white !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background: transparent !important;
    border: 1px solid white !important;
    border-radius: 8px !important;
    color: white !important;
}

/* Remove default grey box */
.stNumberInput, .stSelectbox {
    background: none !important;
}

/* Focus effect */
input:focus {
    border: 1px solid #38bdf8 !important;
    outline: none !important;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #38bdf8);
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

/* Labels */
label {
    color: #cbd5f5 !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.markdown('<div class="title"> Loki Finance Dashboard</div>', unsafe_allow_html=True)

# -------------------- DEFAULT OUTPUT --------------------
if "prob" not in st.session_state:
    st.session_state.prob = 0.0
    st.session_state.score = 0.0
    st.session_state.credit = "None"

# -------------------- OUTPUT SECTION --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="output-card">
        <h4>Default Probability</h4>
        <h2>{st.session_state.prob:.2%}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="output-card">
        <h4>Credit Score</h4>
        <h2>{st.session_state.score:.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="output-card">
        <h4>Credit Status</h4>
        <h2>{st.session_state.credit}</h2>
    </div>
    """, unsafe_allow_html=True)

# -------------------- INPUT SECTION --------------------
st.markdown('<div class="input-card">', unsafe_allow_html=True)

# Row 1
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Age', min_value=18, max_value=100, value=18)
with col2:
    income = st.number_input("Income", min_value=0, value=120000)
with col3:
    loan_Amount = st.number_input("Loan Amount", min_value=0, value=120000)

# Row 2
col4, col5, col6 = st.columns(3)
with col4:
    loan_income_ratio = loan_Amount / income if income > 0 else 0
    st.metric("Loan/Income Ratio", f"{loan_income_ratio:.2f}")
with col5:
    loan_tenure_month = st.number_input('Loan Tenure (Months)', value=0)
with col6:
    avg_dpd_deliquency = st.number_input('Average DPD', value=0)

# Row 3
col7, col8, col9 = st.columns(3)
with col7:
    deliquent_ratio = st.number_input("Delinquency Ratio", min_value=0.0)
with col8:
    credit_utilization_ratio = st.number_input("Credit Utilization Ratio", min_value=0.0)
with col9:
    open_loan_account = st.number_input("Open Loan Accounts", min_value=0)

# Row 4
col10, col11, col12 = st.columns(3)
with col10:
    residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgaged"])
with col11:
    loan_purpose = st.selectbox("Loan Purpose", ["Personal", "Education", "Home", "Auto"])
with col12:
    loan_type = st.selectbox("Loan Type", ["Secured", "Unsecured"])

st.markdown('</div>', unsafe_allow_html=True)

# -------------------- BUTTON --------------------
if st.button("🚀 Predict"):
    prob, score, credit = predict(
        age, income, loan_Amount, loan_tenure_month,
        avg_dpd_deliquency, deliquent_ratio,
        credit_utilization_ratio, open_loan_account,
        residence_type, loan_purpose, loan_type
    )

    # Update session state
    st.session_state.prob = prob
    st.session_state.score = score
    st.session_state.credit = credit

    st.rerun()