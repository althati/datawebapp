import streamlit as st
import pandas as pd



# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Row A
c1, c2 = st.columns((3,3))
with c1:
    st.markdown('### 401K')
    df = pd.read_csv ('/Users/althati/git/datawebapp/stocks.csv')
    st.bar_chart(df,x='profit',y='stock')
    
    
with c2:
    st.markdown('### Annuity')
    df = pd.read_csv ('/Users/althati/git/datawebapp/crypto.csv')
    st.bar_chart(df,x='profit',y='coin')
    
    

# Row B
c1, c2 = st.columns((3,3))
with c1:
    st.markdown('### HSA')
    df = pd.read_csv ('/Users/althati/git/datawebapp/gold.csv')
    st.bar_chart(df,x='profit',y='metal')
    
    
with c2:
    st.markdown('### SSA')
    df = pd.read_csv ('/Users/althati/git/datawebapp/realestate.csv')
    st.bar_chart(df,x='profit',y='property')
    
    
