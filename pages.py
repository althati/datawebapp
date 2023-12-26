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
        Page("pages/retirements.py", "Page 9", ":books:"),
        Page("pages/tax.py", "Page 10", ":books:")
    ]
)