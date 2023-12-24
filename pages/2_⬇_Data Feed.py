import streamlit as st




st.markdown('### Upload Your Data')

file = st.file_uploader("Upload Bank Statements, Credit Card Statements, Tax Statements, and so on", type=["csv"])


st.markdown('### Connect Your Bank and Credit Accounts')

st.multiselect('We use bank-level encryption via Plaid. Safe and Secure. Your Information is protected.', ['Bank Of America', 'Wells Fargo','Chase','Capital One','Discover','American Express','Citi','PNC','US Bank','HSBC','Barclays','Morgan Stanley'])

st.markdown('### Connect Your Stock, Crypto Accounts')

st.multiselect('We use bank-level encryption via Plaid. Safe and Secure. Your Information is protected.', ['Robinhood','Coinbase','TD Ameritrade','Fidelity','Charles Schwab','Etrade','Vanguard','USAA','Ally','Merrill Lynch','Edward Jones','Wells Fargo Advisors','Raymond James','UBS','T Rowe Price','Prudential','Ameriprise','Voya','Principal','Lincoln Financial','MassMutual','John Hancock','New York Life','Northwestern Mutual','Transamerica','Pacific Life','Guardian','Allianz','Nationwide','Thrivent','Brighthouse','Ohio National','AXA','Equitable','RiverSource','Voya','Jackson','Symetra','Minnesota Life','Pacific Life','Protective','Mutual of Omaha','Securian','Penn Mutual','OneAmerica','Foresters','Fidelity & Guaranty Life','American National','Sagicor','American Equity','Global Atlantic','Midland National','Western & Southern','American Fidelity','National Life Group','SBLI','Cincinnati Life','American General','Lincoln Heritage','Oxford Life','AAA Life','Liberty Mutual','AAA Life','Gerber Life','Amica','AAA Life','Auto-Owners'])

st.markdown('### Connect Your Insurance Accounts')

st.multiselect('We use bank-level encryption via Plaid. Safe and Secure. Your Information is protected.', ['Northamerican Company','American National','Sagicor','American Equity','Global Atlantic','Midland National','Western & Southern','American Fidelity','National Life Group','SBLI','Cincinnati Life','American General','Lincoln Heritage','Oxford Life','AAA Life','Liberty Mutual','AAA Life','Gerber Life','Amica','AAA Life','Auto-Owners'])

st.markdown('### Connect Your Social Media Accounts')

st.multiselect('We use bank-level encryption via Plaid. Safe and Secure. Your Information is protected.', ['gmail','facebook','twitter','instagram','linkedin','snapchat','tiktok','youtube','pinterest','reddit','tumblr','flickr','quora','medium','twitch','vimeo','myspace','soundcloud','deviantart','meetup','goodreads','dribbble','slack','discord'])


