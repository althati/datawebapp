import streamlit as st
import pandas as pd



# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Row A
c1, c2 = st.columns((3,3))
with c1:
    st.markdown('### Fees')
    df = pd.read_csv ('data/stocks.csv')
    st.bar_chart(df,x='profit',y='stock')
    
    
with c2:
    st.markdown('### Purchases')
    df = pd.read_csv ('data/crypto.csv')
    st.bar_chart(df,x='profit',y='coin')
    
    


