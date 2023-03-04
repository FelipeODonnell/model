
import streamlit as st
import pandas as pd
import webbrowser


url = 'https://felipeodonnell-model-main-ryfv0j.streamlit.app'



with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Blueblocks.ai")
    if st.button('All MVP Solutuons'):
        webbrowser.open_new_tab(url)

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

current_payment = st.number_input("Enter your current monthly variable mortgage payment:", min_value=0.01, step=0.01)
outstanding_amount = st.number_input("Enter your outstanding mortgage amount:", min_value=0.01, step=0.01)

if st.button("Calculate"):
    fixed_payment = calculate_fixed_payments(current_payment, outstanding_amount)
    st.write("Your monthly fixed mortgage payment per month would be:", fixed_payment/12)
    cash_flows = calculate_cash_flows(fixed_payment/12, outstanding_amount)
    cash_flows_df = pd.DataFrame({"Month": range(1, 13), "Payment": cash_flows})
    st.write("Monthly cash flows for the fixed payments:")
    st.dataframe(cash_flows_df)



