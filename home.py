import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Page("pages/accounts.py", "Page 1", ":books:"),
        Page("pages/contact.py", "Page 2", ":books:"),
        Page("pages/data_feed.py", "Page 3", ":books:"),
        Page("pages/health.py", "Page 4", ":books:"),
        Page("pages/home.py", "Page 5", ":books:"),
        Page("pages/insurance.py", "Page 6", ":books:"),
        Page("pages/investments.py", "Page 7", ":books:"),
        Page("pages/kids.py", "Page 8", ":books:"),
        Page("pages/retrirements.py", "Page 9", ":books:"),
        Page("pages/tax.py", "Page 10", ":books:")
    ]
)


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
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







st.video('https://www.youtube.com/watch?v=RjiqbTLW9_E&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW')


st.text("")
st.text("")
st.text("")
st.text("")
st.write("Download our app from the App Store or Google Play Store.")
st.image("https://pureoxygenlabs.com/wp-content/uploads/2020/07/icons-app-store-google-play-250x250-LL.png")
