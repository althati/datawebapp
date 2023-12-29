import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("home.py", "Home", "🏠"),

        #Section(name="Stocks 1", icon="📈"),
        Page("pages/data_feed.py", "Feed the Data", "🌥️"),

        Page("pages/stocks.py", "Stocks Analysis", "📈"),

        Page("pages/accounts.py", "Your Accounts", ":books:"),

        Page("pages/health.py", "Your Health", "💗"),

        #Section(name="Retirements 1", icon="👴"),

        Page("pages/home.py", "Your Home Maintainance", "🛋️"),

        Page("pages/insurance.py", "Your Schedule", "📅"),

        #Section(name="Health 1", icon="💗"),

        Page("pages/kids.py", "Your Family", "👨‍👩‍👦‍👦"),
             
        Page("pages/insurance.py", "Your Insurance", "☂️"),

        Page("pages/investments.py", "Your Investements", "💸"),

        Page("pages/retirements.py", "Your Retirement", "👴"),
        
        Page("pages/tax.py", "Your Tax", "💰"),

        #Page("pages/robinhood.py", "Page 11", ":books:"),

        Page("pages/powerbi.py", "Testing", "🍌"),

        Page("pages/contact.py", "Contact", "☎️"),

        
    ]
)




st.write("# Welcome to My Analytics! 👋")

st.markdown(
    """
    My Analytics is an app built specifically for individuals who want to analyze their own data using data visualizations.
    Users can upload their own data or they can pull their own data from various sources by securly connecting to their accounts. 
    Users can setup alerts to be notified when certain thresholds are met.
    Machine Learning models can be trained to predict future outcomes, find ways to save money, and much more.
    """
)


st.video('https://youtu.be/OO2nDVReF7w?si=WJdQo9IGw6brF33l')


st.text("")
st.text("")
st.text("")
st.text("")
st.write("Download our app from the App Store or Google Play Store.")
st.image("https://pureoxygenlabs.com/wp-content/uploads/2020/07/icons-app-store-google-play-250x250-LL.png")
