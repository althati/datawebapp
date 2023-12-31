import streamlit as st
import base64

st.set_page_config(layout="wide")

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

 
    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1450" height="750" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)



def year_picker(label, key):
    years = ["2022", "2023"]
    st.selectbox(label, options=years, key=key, on_change=selection)

def selection():
    file_name = "data/personal/paystubs/"+st.session_state.source_year+ "_paystub_sample.pdf"
    displayPDF(file_name)

year_picker("Year", "source_year")

