import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from config import DATA_PATH




def run():
    df = pd.read_csv(DATA_PATH)
    eda_options = st.sidebar.selectbox('Select EDA Option', ['Show Data', 
                                                          'Missing Values',
                                                          'Categorical Analysis',
                                                          'Numerical Analysis'])
    
    if eda_options == 'Show Data':
        st.subheader('Raw Dataset')
        st.dataframe(df.head(4))
        