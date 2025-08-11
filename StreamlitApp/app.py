import streamlit as st
from sections import EDA , Train #, ModelInference


st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'EDA', 'Model Training', 'Model Inference'])

if page == 'Home':
    st.title('Load Predition App')
    st.markdown('#### ML-Powered web App to predict loan status')
    
    st.markdown("---")
    col1, col2 = st.columns([2,1])
    with col1: 
        st.markdown("""
                    ### About this project
                    This app uses machine learning to predict whether a loan application will be approved or not.
                    """
                    )
    with col2:
        st.markdown("""
                    ## Enter Anything
                    """)
        st.success('Use the sidebar to navigate through the app')
        
elif page == 'EDA':
    EDA.run()
    
elif page == 'Model Training':
    Train.run()
    