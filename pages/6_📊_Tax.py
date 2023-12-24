import streamlit as st
import pandas as pd



# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Row A
c1, c2 = st.columns((3,3))
with c1:
    st.markdown('### Income Tax')
    df = pd.read_csv ('data/stocks.csv')
    st.bar_chart(df,x='stock',y='profit')
    
    
with c2:
    st.markdown('### Property Tax')
    df = pd.read_csv ('data/crypto.csv')
    st.bar_chart(df,x='coin',y='profit')
    
    

# Row B
c1, c2 = st.columns((3,3))
with c1:
    st.markdown('### Medicare Tax')
    df = pd.read_csv ('data/gold.csv')
    st.bar_chart(df,x='metal',y='profit')
    
    
with c2:
    st.markdown('### Social Security Tax')
    df = pd.read_csv ('data/realestate.csv')
    st.bar_chart(df,x='property',y='profit')
    
    
