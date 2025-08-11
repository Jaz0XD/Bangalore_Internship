import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from config import DATA_PATH
from utils import get_missing_value_graph, categorical_graph, get_histogram, kde_plot



def run():
    
    st.session_state['data'] = pd.read_csv(DATA_PATH)
    st.session_state['data'] = st.session_state['data'].drop(columns=['Loan_ID'])
    eda_options = st.sidebar.selectbox('Select EDA Option', ['Show Data', 
                                                          'Missing Values',
                                                          'Categorical Analysis',
                                                          'Numerical Analysis'])
    
    if eda_options == 'Show Data':
        st.subheader('Raw Dataset')
        st.dataframe(st.session_state['data'].head(4))
    elif eda_options == 'Missing Values':
        graph = get_missing_value_graph(st.session_state['data'])
        st.pyplot(graph)
    elif eda_options == 'Categorical Analysis':
        st.subheader('Categorical Analysis')
        cat_columns = st.session_state['data'].select_dtypes(include=['object']).columns.tolist()
        selected_cat = st.selectbox('Select Categorical Column', cat_columns)
        graph = categorical_graph(st.session_state['data'], selected_cat)
        st.pyplot(graph)
    elif eda_options == 'Numerical Analysis':
        st.subheader('Numerical Analysis')
        selected_num = st.selectbox('Select Graph Type',['Histogram', 'KDE'])
        if selected_num == 'Histogram':
            graph = get_histogram(st.session_state['data'])
        elif selected_num == 'KDE':
            graph = kde_plot(st.session_state['data'])
        st.pyplot(graph)
    