import streamlit as st

st.set_page_config(layout="wide")

st.title("Contact")

st.text_input('Full Name')


st.text_input('Address')


st.text_input('Email')


st.text_input('Phone')


st.button('Submit')