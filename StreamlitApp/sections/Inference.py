import pickle
import streamlit as st
import pandas as pd

from utils import categorical_encoding
from config import DATA_PATH

def run():
    st.title("Loan Status Prediction")
    st.write("Enter the applicant's details to predict loan approval status.")
    
    # Load the original data to get column structure
    if 'original_data' not in st.session_state:
        st.session_state['original_data'] = pd.read_csv(DATA_PATH)
    
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Marital Status", ["Yes", "No"])
    dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_amount_term = st.number_input("Loan Term (in months)", min_value=0)
    credit_history = st.selectbox("Credit History", [1.0, 0.0])
    property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])
    
    input_data = pd.DataFrame([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_amount_term,
        credit_history,
        property_area
    ]], columns=[
        'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
        'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 
        'Loan_Amount_Term', 'Credit_History', 'Property_Area'
    ])
    
    st.subheader("Input Data:")
    st.dataframe(input_data)
    
    if st.button("Predict"):
        
        processed_data = input_data.copy()    
        cat_cols = [col for col in processed_data.columns if processed_data[col].dtype == object]
        processed_data = categorical_encoding(processed_data, cat_cols)
        
        with open('models/Decision Tree.pkl', 'rb') as f:
            trained_model = pickle.load(f)
        
        prediction = trained_model.predict(processed_data)[0]
        
        st.subheader("Prediction Result:")
        if prediction == 1:
            st.success("🎉 Loan Approved!")
        else:
            st.error("❌ Loan Not Approved")
            
        st.subheader("Processed Input Data:")
        st.dataframe(processed_data)