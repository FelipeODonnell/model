import streamlit as st
import pandas as pd
import webbrowser

st.title('UK Instant Home Valuation Estimate')


url = 'https://felipeodonnell-model-main-ryfv0j.streamlit.app'

with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Blueblocks.ai")
    if st.button('All MVP Solutuons'):
        webbrowser.open_new_tab(url)

df = pd.read_csv('propdata.csv', index_col='Postcode')
# Get user input for postcode, number of bedrooms, and contract length
x_raw = st.text_input('Please enter your postcode: (Caps and no spaces)')
rooms = st.text_input('How many bedrooms does the property have:' )
# Adjust postcode input
x = x_raw[:-3]
# Check if postcode exists in dataframe
if x not in df.index:
    st.error('The postcode you entered does not exist in the dataframe.')
else:
    # Show postcode data
    st.write('Data for postcode', x)
    st.write(df.loc[[x]])

    # Find the column to get data from
    bedroom_col = 'Avg asking price ('+str(rooms)+' bed)'

    # Check if column exists in dataframe
    if bedroom_col not in df.columns:
        st.error('The number of bedrooms you entered does not exist as a column in the dataframe.')
    else:
        p1 = df.loc[[x], bedroom_col]
        p2 = p1.convert_dtypes()
        p3 = p2.str.replace(",","")
        p4 = p3.astype(float, errors = 'raise')
        p = int(p4)
        st.write('The Average asking price in the postcode for the number of bedrooms entered is:', p)