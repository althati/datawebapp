import streamlit as st
import pandas as pd



# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Row A
c1, c2 = st.columns((3,3))
with c1:
    st.markdown('### Health')
    df = pd.read_csv ('data/stocks.csv')
    st.bar_chart(df,x='stock',y='profit')
    
    
with c2:
    st.markdown('### Life')
    df = pd.read_csv ('data/crypto.csv')
    st.bar_chart(df,x='coin',y='profit')
    
    

# Row B
c1, c2 = st.columns((3,3))
with c1:
    st.markdown('### Home')
    df = pd.read_csv ('data/gold.csv')
    st.bar_chart(df,x='metal',y='profit')
    
    
with c2:
    st.markdown('### Auto')
    df = pd.read_csv ('data/realestate.csv')
    st.bar_chart(df,x='property',y='profit')
    
    
