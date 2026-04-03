import streamlit as st
from Prediction_helper import predict
st.title("Loki Finance: Credit Portal")

# Row 1
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Age',min_value=18,max_value=100,value=18,step=1)
with col2:
    income = st.number_input("Income",min_value=0,value=120000)
with col3:
    loan_Amount = st.number_input("Loan_amount",min_value=0,value=120000)

# Row 2
col4, col5, col6 = st.columns(3)
with col4:
    loan_income_ratio = loan_Amount/income if income>0 else 0
    st.text("loan income ratio")
    st.text(f'{loan_income_ratio:.2f}')
with col5:
    loan_tenure_month = st.number_input('Loan tenure (month)',value=0,step=1)
with col6:
    avg_dpd_deliquency = st.number_input('Average DPD',value=0,step=1)

# Row 3
col7, col8, col9 = st.columns(3)
with col7:
    deliquent_ratio = st.number_input("Delinquency Ratio", min_value=0.0)
with col8:
    credit_utilization_ratio = st.number_input("Credit Utilization Ratio", min_value=0.0)
with col9:
    open_loan_account = st.number_input("Open Loan Account", min_value=0)

# Row 4
col10, col11, col12 = st.columns(3)
with col10:
    residence_type = st.selectbox(
        "Residence Type",
        ["Owned", "Rented", "Mortgaged"]
    )
with col11:
    loan_purpose = st.selectbox(
        "Loan Purpose",
        ["Personal", "Education", "Home","Auto"]
    )
with col12:
    loan_type = st.selectbox(
        "Loan Type",
        ["Secured", "Unsecured"]
    )

# Submit button
if st.button("Submit"):
    prob , score , credit = predict(age,income,loan_Amount,loan_tenure_month,avg_dpd_deliquency,deliquent_ratio,credit_utilization_ratio,open_loan_account,residence_type,loan_purpose,loan_type)
    st.success(f'{prob:.2%}')
    st.success(f'{score:.2f}')
    st.success(credit)