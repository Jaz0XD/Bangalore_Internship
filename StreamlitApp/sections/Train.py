# Importing Dependencies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pickle
import os

# Importing Sklearn libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import MinMaxScaler

# Importing Files & Functions
from utils import fill_na, categorical_encoding
from config import (CAT_COLS, CONT_COLS, MODEL_SAVE_PATH)

def run():
    st.title('Model Training')
    st.subheader('DataSet Preview')
    st.dataframe(st.session_state['data'].head(4))
    st.subheader('Missing Value Handling')
    fill_method = st.radio('Choose Imputation method for numeric features', ['Mean', 'Median', 'Mode'])
    st.session_state['filled_data'] = fill_na(st.session_state['data'].copy(), fill_method)
    df_encoded = categorical_encoding(st.session_state['filled_data'], CAT_COLS)

    if st.button('Perform Scaling'):
        st.session_state['scaler'] = MinMaxScaler()
        st.success('Data Frame successfully scaled')
        df_encoded[CONT_COLS] = st.session_state['scaler'].fit_transform(df_encoded[CONT_COLS])
        st.dataframe(df_encoded.head(4))

    x = df_encoded.drop(columns=['Loan_Status'])
    y= df_encoded['Loan_Status']
    X_train, X_test , y_train, y_test = train_test_split(x,y,test_size = 0.1, random_state=42)
    model_text = st.selectbox('Select Model', ['Random Forest', 'Decision Tree', 'Logistic Regression'])
    if st.button('Train Model'):
        
        if model_text == 'Random Forest':
            rf_model = RandomForestClassifier()
            rf_model.fit(X_train, y_train)
            y_pred = rf_model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)
            st.text(f'Classification Report:')
            st.code(report)
            save_path = os.path.join(MODEL_SAVE_PATH, model_text + '.pkl')
            with open(save_path, 'wb') as f:
                pickle.dump(rf_model, f)
            st.success('Random Forest model trained and saved successfully!')

        elif model_text == 'Decision Tree':
            dt_model = DecisionTreeClassifier()
            dt_model.fit(X_train, y_train)
            y_pred = dt_model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)
            st.text(f'Classification Report:')
            st.code(report)
            save_path = os.path.join(MODEL_SAVE_PATH, model_text + '.pkl')
            with open(save_path, 'wb') as f:
                pickle.dump(dt_model, f)
            st.success('Decision Tree model trained and saved successfully!')
            
        elif model_text == 'Logistic Regression':
            lr_model = LogisticRegression()
            lr_model.fit(X_train, y_train)
            y_pred = lr_model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)
            st.text(f'Classification Report:')
            st.code(report)
            save_path = os.path.join(MODEL_SAVE_PATH, model_text + '.pkl')
            with open(save_path, 'wb') as f:
                pickle.dump(lr_model, f)
            st.success('Logistic Regression model trained and saved successfully!')