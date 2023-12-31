# streamlit_app.py

import streamlit as st
import time 
from sqlalchemy.sql import text

# Initialize connection.
conn = st.connection('mysql', type='sql')


def store_in_db(data: dict):
    # Example: Inserting data into the table
    with conn.session as s:
        for k in data:
            s.execute(text('INSERT INTO mytable2 (key2, value2) VALUES (:key2, :value2);'), params=dict(key2=k, value2=data[k]))
            
        s.commit()
        # Perform query.
    
    df = conn.query('SELECT * from mytable2;', ttl=600)

    # Print results.
    st.write(df)


st.header("Budget Planning")

form = st.form(key="match")
with form:
    
    month = st.selectbox("Choose Month", (1,2,3,4,5,6,7,8,9,10,11,12))
    paycheck = st.number_input("Pay Check")
    home_emi = st.number_input("Home EMI")
    home_maintanence_insurance = st.number_input("Home Maintanence - Insurance")
    home_maintanence_tax = st.number_input("Home Maintanence - Property Tax")
    home_maintanence_hoa = st.number_input("Home Maintanence - HOA")
    home_maintanence_lawncare = st.number_input("Home Maintanence - Lawncare")
    home_maintanence_cleaning = st.number_input("Home Maintanence - Cleaning")
    auto_emi = st.number_input("Auto EMI")
    auto_maintanence_insurance = st.number_input("Auto Maintanence - Insurance")
    auto_maintanence_servicing = st.number_input("Auto Maintanence - Servicing")
    grocery = st.number_input("Grocery")
    internet = st.number_input("Internet")
    phone = st.number_input("Phone")
    power = st.number_input("Power")
    gas = st.number_input("Gas")

    timestamp = time.time()
    submit = st.form_submit_button("Submit")
    if submit:
        store_in_db({"month": month, 
                     "paycheck": paycheck, 
                     "home_emi": home_emi, 
                     "home_maintanence_insurance": home_maintanence_insurance, 
                     "home_maintanence_tax": home_maintanence_tax, 
                     "home_maintanence_hoa": home_maintanence_hoa, 
                     "home_maintanence_lawncare": home_maintanence_lawncare, 
                     "home_maintanence_cleaning": home_maintanence_cleaning, 
                     "auto_emi": auto_emi, 
                     "auto_maintanence_insurance": auto_maintanence_insurance, 
                     "auto_maintanence_servicing": auto_maintanence_servicing, 
                     "grocery": grocery, 
                     "internet": internet, 
                     "phone": phone,
                     "power": power, 
                     "gas": gas, })




