import streamlit as st
import pandas as pd
import plotly.express as px


# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Row A
c1, c2 = st.columns((3,3))
with c1:
    st.markdown('### Income Tax')
    df = pd.read_csv ('/Users/althati/git/datawebapp/stocks.csv')
    fig=px.bar(df,x='profit',y='stock', orientation='h',text=df['profit'].apply(lambda x: '{0:1.2f}%'.format(x)))
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.write(fig)
with c2:
    st.markdown('### Property Tax')
    df = pd.read_csv ('/Users/althati/git/datawebapp/crypto.csv')
    fig=px.bar(df,x='profit',y='coin', orientation='h',text=df['profit'].apply(lambda x: '{0:1.2f}%'.format(x)))
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.write(fig)

# Row B
c1, c2 = st.columns((3,3))
with c1:
    st.markdown('### Medicare Tax')
    df = pd.read_csv ('/Users/althati/git/datawebapp/gold.csv')
    fig=px.bar(df,x='profit',y='metal', orientation='h',text=df['profit'].apply(lambda x: '{0:1.2f}%'.format(x)))
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.write(fig)
with c2:
    st.markdown('### Social Security Tax')
    df = pd.read_csv ('/Users/althati/git/datawebapp/realestate.csv')
    fig=px.bar(df,x='profit',y='property', orientation='h',text=df['profit'].apply(lambda x: '{0:1.2f}%'.format(x)))
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.write(fig)
