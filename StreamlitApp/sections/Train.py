import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import fill_na, categorical_encoding
from sklearn.preprocessing import MinMaxScaler
from config import CAT_COLS, CONT_COLS

def run():
    st.title('Model Training')
    st.subheader('DataSet Preview')
    st.dataframe(st.session_state['data'].head(4))
    st.subheader('Missing Value Handling')
    fill_method = st.radio('Choose Imputation method for numeric features', ['Mean', 'Median', 'Mode'])
    st.session_state['filled_data'] = fill_na(st.session_state['data'].copy(), fill_method)
    df_encoded = categorical_encoding(st.session_state['filled_data'], CAT_COLS)

    if st.button('Perform Scaling'):
        scaler = MinMaxScaler()
        df_encoded[CONT_COLS] = scaler.fit_transform(df_encoded[CONT_COLS])
        st.dataframe(df_encoded.head(4))