import os
BASE_DIR = os.getcwd()
MODEL_SAVE_PATH = os.path.join(BASE_DIR, 'models')

DATA_PATH = "D:\PROJECT\StreamlitApp\data\loan_data.csv"

CAT_COLS = ['Gender',
 'Married',
 'Dependents',
 'Education',
 'Self_Employed',
 'Property_Area',
 'Loan_Status']

CONT_COLS = ['ApplicantIncome',
 'CoapplicantIncome',
 'LoanAmount',
 'Loan_Amount_Term',
 'Credit_History']
