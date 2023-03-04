
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import webbrowser


url = 'https://felipeodonnell-model-main-ryfv0j.streamlit.app'

with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Blueblocks.ai")
    if st.button('All MVP Solutuons'):
        webbrowser.open_new_tab(url)


# Load historical UK property data
data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
data = pd.read_csv(data_url, header=None, delimiter=r"\s+", names=columns)

# Define function to calculate future prices
def calc_future_prices(purchase_price, rental_price):
    # Calculate annual growth rates from historical data
    purchase_growth = np.mean(data['MEDV'].pct_change())
    rental_growth = np.mean(data['RM'].pct_change())

    # Calculate future prices for every year for the next 7 years
    future_purchase_prices = []
    future_rental_prices = []
    for year in range(1, 11):
        future_purchase_price = purchase_price * (1 + purchase_growth)**year
        future_rental_price = rental_price * (1 + rental_growth)**year
        future_purchase_prices.append(future_purchase_price)
        future_rental_prices.append(future_rental_price)

    future_prices_df = pd.DataFrame({
        'Year': range(1, 11),
        'Future Purchase Price': future_purchase_prices,
        'Future Rental Price': future_rental_prices
    })

    return future_prices_df

# Define Streamlit app
st.title('Future Property Prices')
st.write('Enter the current sale and rental price of your property in the UK:')
purchase_price = st.number_input('Sale Price', value=0)
rental_price = st.number_input('Rental Price', value=0)

if st.button('Calculate Future Prices'):
    # Calculate future prices
    future_prices_df = calc_future_prices(purchase_price, rental_price)

    # Add purchase offer and rental offer columns to the dataframe
    purchase_offer = 0.9
    rental_offer = 0.8
    future_prices_df['Purchase Offer'] = future_prices_df['Future Purchase Price'] * purchase_offer
    future_prices_df['Rental Offer'] = future_prices_df['Future Rental Price'] * rental_offer

    # Display future prices in a table
    st.write(future_prices_df)

    # Plot future price vs year
    fig1, ax1 = plt.subplots()
    ax1.plot(future_prices_df['Year'], future_prices_df['Future Purchase Price'])
    ax1.set_title('Future Purchase Price vs Year')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Future Purchase Price (£)')
    st.pyplot(fig1)

    # Plot future rental vs price
    fig2, ax2 = plt.subplots()
    ax2.plot(future_prices_df['Year'], future_prices_df['Future Rental Price'])
    ax2.set_title('Future Rental Price vs Year')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Future Rental Price (£)')
    st.pyplot(fig2)

    