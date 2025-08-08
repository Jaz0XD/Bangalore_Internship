import streamlit as st
import pandas as pd

st.title('Streamlit Basics')
st.header('This is the Header')
st.subheader('this is a subheader')
st.text('This is some text')
st.caption('This is a caption')


name = st.text_input('Enter your name', placeholder='Type here...')

st.write(f'Your name is {name}')
age = st.number_input('Enter your age', min_value=0, max_value=120, value=25)
st.write(f'Your age is {age}')


st.slider('Select level', 0, 100)
st.text_area('Enter your bio')
st.checkbox('I agree to the T&C')
st.radio('Select your gender', ['Male', 'Female'])
st.selectbox('Select your country', ['USA', 'Canada', 'UK', 'Australia'])
st.button('Submit')
st.success('Form submitted successfully!')
st.warning('Please fill out all fields.')
st.progress(69)

tab1, tab2, tab3 =st.tabs([
    "Dataset",
    "Head",
    "Tail"
])
df = pd.read_csv("D:\PROJECT\Housing.csv")
with tab1:
    st.dataframe(df)
with tab2:
    st.dataframe(df.head(5))
with tab3:
    st.dataframe(df.tail(5))


st.sidebar.title('Sidebar Title')
st.sidebar.header('Sidebar Header')

st.markdown('This is some **bold** text in the sidebar')


col1, col2 = st.columns([2,1])
with col1:
    st.write('This is some text in the first column.')

with col2:
    st.write('This is some text in the second column.')