import streamlit as st
import pandas as pd

import streamlit as st
import plotly.express as px 


# Page setting
st.set_page_config(layout="wide")

#with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Row A


st.markdown('### Sold View')
sold_df = pd.read_csv('data/robinhood/soldview.csv').sort_values(by='profit',ascending=True).reset_index(drop=True)
fig=px.bar(sold_df,x='profit',y='stock', orientation='h',text_auto=True,text='profit')
st.write(fig)

profit_sum = sold_df['profit'].sum()
st.write("Total Profit:", profit_sum)



st.markdown('### Hold View - Profit')
hold_df1 = pd.read_csv('data/robinhood/holdview1.csv').sort_values(by='unrealized_profit',ascending=True).reset_index(drop=True)
fig=px.bar(hold_df1,x='unrealized_profit',y='stock', orientation='h',text_auto=True,text='unrealized_profit')
st.write(fig)

unrealized_profit_sum = hold_df1['unrealized_profit'].sum()
st.write("Total Unrealized Profit:", unrealized_profit_sum)

st.markdown('### Hold View - Loss')
hold_df2 = pd.read_csv('data/robinhood/holdview2.csv').sort_values(by='unrealized_profit',ascending=True).reset_index(drop=True)
fig=px.bar(hold_df2,x='unrealized_profit',y='stock', orientation='h',text_auto=True,text='unrealized_profit')
st.write(fig)

unrealized_profit_sum = hold_df2['unrealized_profit'].sum()
st.write("Total Unrealized Loss:", unrealized_profit_sum)