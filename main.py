'''
****
Create a virtual environment

Used to create env:
python3 -m venv DLpricer

Activate:
source DLpricer/bin/activate

Deactive:
deactivate


***

To run
streamlit run main.py

Types of learning models to try
Multi-layer perceptron (MLP)
Convolutional neural network (CNN) 
Recurrent neural network (RNN)
Long short-term memory (LSTM)
'''


#Import 
from operator import index
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 
from scipy.stats import norm
import altair as alt


with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Blueblocks.ai")
    choice = st.radio("Navigation", ["Overview", "Valuation","Structuring","Swaps", "Market"])
    st.info("This project application helps you get instant valuations and structures solutions for your property")


if choice == "Overview":
    st.title('Overview')
    '''

        Blueblock.ai

     Real Estate Financial Engineering

    Offering automated structured solutions for participants in the residential market


        Navigation Guide:
    
    Valuation - This gives a simple model with postcode and bedrooms as to the average price in the area (this is simplified but from the valuation you can give options for the user to contact a local agent or see structured deals avaliable)
    
    Forward - Example of the type of offerings a forward market may look like
    
    Swaps - Provides a quote for customers who want to protect their variable mortgage payments from going up by entering a swap for which they agree fixed payments
    
    Market - Example of what a interface may look like for a synthethic marketplace



    

        Business Questions:

    **Describe the problem your business is solving 300 characters**

   The residential UK property market has huge inefficiencies and being a landlord is the worst asset to own. Its difficult, expansive and slow to do almost anything, from buying to selling, renting, fixing issues, mortgages, taxation. Part of this is intrinsic to the nature of the asset being complex, namely the upkeep of the property, but other aspects are unnecessarily complex and beaurocratic. Technology has been naturally deflationary and increased speed and ease in other industries but not the real estate market yet. There have been some innovations such as Rightmove which have done a great job, but this has unfortunately only addressed the accessibility of information in the market, not the underlying mechanisms of doing any of the previously mentioned issues. Financial engineering in the form of derivative products have led to incredible innovations in the world of finance and the ability for business' to protect themselves from risk and to get the best deals to suit them and their situation, these innovations havnt been brought to customers and individuals as of yet however. Partially due to it being more profitable to focus on high volume markets like bonds and equities, and partially due to regulation. 

    **Describe how you are solving the problem mentioned above. 300 characters**

    Blueblock offers solutions to the inefficiencies in the residential UK property market by providing automated derivative solutions, a fixed/variable mortgage rate swap, forward purchase pricing, and an instant pricing model as the first products. These financial engineering and derivatives tools provide more options for landlords and investors, making the market more efficient and accessible with greater transparency.


    **What are the objections/greatest challenges to your idea?**

    The greatest challenges to the idea are regulatory hurdles, lack of awareness and understanding of financial engineering and derivatives in the property market, and potential resistance from traditional market participants.

    Model - if the model isnt accurate and provide valuable information, customers will use other instant valuation models

    Legal - Real estate is a regulated market and especially with derivatives

    Structured solutions - If the structured solutions offer is not clear and transparent it will not be used


    **Main competitors?**

    No direct competitors for a market for real estate derivatives, indirect competitors include other instant valuation companies (onthemarket.co.uk, Zoopla - however these require sign ups and are instant sales pitches)

    Other indirect competitors are companies which provide rent to own schemes (potentially a competitor for the market for forward purchases/options )

    Lenders are a competitor for fixed/variable products but operated expensively and slowly

    **How do you differentiate from competitors?**

    No other player in the industry offers a market for real estate derivatives

    Players who do offer fix/varible financing products are lenders and changing these products takes months and there is a large fee for product changes')



    
        Future potential:
    Derivatives Exchange - buyers/sellers can list and offer on a market for structured deals (e.g. Forward contract - a person lists to sell their house in 5 years time for 100k to protect from market downturn), OR (Option contract - the buyer (person who agree to buy the house in 5y), decides he isnt sure he wants to do the deal in 5 years so instead of being obliged to as he would be in a forward contract, she pays the seller 1k today, so that he has the option in 5y when it come time for the deal, to not go ahead with it if he wishes). - With this exchange market making is also possible which would be hugely profitable in a inefficient market like the real estate one if done correctly


    Tokenisation of assets - Ledger tech provides huge potential in tokenisation of assets, specifically the tokenisation of real estate derivatives - the land registry department will not adopt blockchain ledgers for a few decades but if you are able to make a market for derivatives and use blockchain to keep track of the transactions, not only will it be significantly more efficient in cost, but also there is be no barriers stopping this


    Synthetic markets - This may be a potential to provide liquid market securities for more localised markets, such as Leeds, or warehouses in London, where investors can get exposure to these niche markets 


    
    '''


if choice == "Valuation":
    st.title('Property Area Valuation')
    st.write('This gives data about the local area of the postcode entered')
    st.write('This product is free and is to drive usage, anyone can check a postcode and instantly get data about the property and local area. There will be options for users to sell their property now, which will reffer them to an agent. Or to list it on the derivatives market, where they can list the property themselves and review offers for current or future purchases of the property')
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




if choice == "Structuring": 
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
        for year in range(1, 8):
            future_purchase_price = purchase_price * (1 + purchase_growth)**year
            future_rental_price = rental_price * (1 + rental_growth)**year
            future_purchase_prices.append(future_purchase_price)
            future_rental_prices.append(future_rental_price)
        
        return future_purchase_prices, future_rental_prices

    # Define Streamlit app
    st.title('Future Property Prices')
    st.write('This product would be integrated into the valuation offering, enabling users to see the expected value of their property at future dates')
    st.write('Enter the current sale and rental price of your property in the UK:')
    purchase_price = st.number_input('Sale Price', value=0)
    rental_price = st.number_input('Rental Price', value=0)


    if st.button('Calculate Future Prices'):
        # Calculate future prices
        future_purchase_price, future_rental_price = calc_future_prices(purchase_price, rental_price)
        
        # Display future prices in a table
        future_prices_df = pd.DataFrame({'Year': range(1, 8), 
                                        'Future Purchase Price': future_purchase_price, 
                                        'Future Rental Price': future_rental_price})
        st.write(future_prices_df)
        
        # Plot future price vs year
        fig1, ax1 = plt.subplots()
        ax1.plot(range(1, 8), future_purchase_price)
        ax1.set_title('Future Purchase Price vs Year')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Future Purchase Price (£)')
        st.pyplot(fig1)
        
        # Plot future rental vs price
        fig2, ax2 = plt.subplots()
        ax2.plot(future_purchase_price, future_rental_price)
        ax2.set_title('Future Rental Price vs Future Purchase Price')
        ax2.set_xlabel('Future Purchase Price (£)')
        ax2.set_ylabel('Future Rental Price (£)')
        st.pyplot(fig2)


if choice == "Swaps": 
    def calculate_fixed_payments(current_payment, outstanding_amount):
    # Calculate the monthly fixed mortgage payment for the next year with a 10% fee
        fixed_payment = (current_payment * 1.15) * 12
        return fixed_payment

    def calculate_cash_flows(fixed_payment, outstanding_amount):
        # Calculate the monthly cash flows for the fixed payments
        cash_flows = []
        balance = outstanding_amount
        for i in range(12):
            interest = balance * 0.05 / 12
            principal = fixed_payment - interest
            balance -= principal
            cash_flows.append(fixed_payment)
        return cash_flows

    st.title("Mortgage Payment Calculator")
    st.write('This product enables users to enter a swap, that allows them to change from a variable rate mortgage to a fix with an instant quote and contract, as well as change from a fixed to variable')

    current_payment = st.number_input("Enter your current monthly variable mortgage payment:", min_value=0.01, step=0.01)
    outstanding_amount = st.number_input("Enter your outstanding mortgage amount:", min_value=0.01, step=0.01)

    if st.button("Calculate"):
        fixed_payment = calculate_fixed_payments(current_payment, outstanding_amount)
        st.write("Your fixed mortgage payment per month for a year long contract would be:", int(fixed_payment/12))
        cash_flows = calculate_cash_flows(fixed_payment/12, outstanding_amount)
        cash_flows_df = pd.DataFrame({"Month": range(1, 13), "Payment": cash_flows})
        st.write("Monthly cash flows for the fixed payments:")
        st.dataframe(cash_flows_df)
            

if choice == "Market": 
    st.title("Example of Derivatives Securities Market")
    st.write('This is an example of a security on the real estate market, this would allow investors to buy and sell forward and options contracts, this would be possible with individual properties as well as securities to track prices in certain areas, Blueblock would provide liquidity on this market, investors in securities would be institutions, buyers and sellers of properties would typically be individuals')
    st.image('Data/333368727_567698838713526_2956667945644696937_n.jpg')