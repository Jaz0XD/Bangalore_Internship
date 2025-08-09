import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from config import DATA_PATH
from utils import get_missing_value_graph, categorical_graph, get_histogram, kde_plot



def run():
    df = pd.read_csv(DATA_PATH)
    df = df.drop(columns=['Loan_ID'])
    eda_options = st.sidebar.selectbox('Select EDA Option', ['Show Data', 
                                                          'Missing Values',
                                                          'Categorical Analysis',
                                                          'Numerical Analysis'])
    
    if eda_options == 'Show Data':
        st.subheader('Raw Dataset')
        st.dataframe(df.head(4))
    elif eda_options == 'Missing Values':
        graph = get_missing_value_graph(df)
        st.pyplot(graph)
    elif eda_options == 'Categorical Analysis':
        st.subheader('Categorical Analysis')
        cat_columns = df.select_dtypes(include=['object']).columns.tolist()
        selected_cat = st.selectbox('Select Categorical Column', cat_columns)
        graph = categorical_graph(df, selected_cat)
        st.pyplot(graph)
    elif eda_options == 'Numerical Analysis':
        st.subheader('Numerical Analysis')
        selected_num = st.selectbox('Select Graph Type',['Histogram', 'KDE'])
        if selected_num == 'Histogram':
            graph = get_histogram(df)
        elif selected_num == 'KDE':
            graph = kde_plot(df)
        st.pyplot(graph)
    