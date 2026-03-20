import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("fraud_model.pkl")

st.title("Bank Transaction Fraud Detection System")

st.write("Enter transaction details:")

# ------------------ INPUTS ------------------

# Gender (Dropdown)
gender = st.selectbox("Gender", ["Male", "Female"])
Gender = 1 if gender == "Male" else 0

# Numeric Inputs
Age = st.number_input("Age", min_value=0)
Transaction_Amount = st.number_input("Transaction Amount", min_value=0)
Account_Balance = st.number_input("Account Balance", min_value=0)

# Transaction Type
transaction_type = st.selectbox(
    "Transaction Type",
    ["Online", "ATM", "POS"]
)
if transaction_type == "Online":
    Transaction_Type = 0
elif transaction_type == "ATM":
    Transaction_Type = 1
else:
    Transaction_Type = 2

# Merchant Category
merchant_category = st.selectbox(
    "Merchant Category",
    ["Shopping", "Food", "Travel", "Bills"]
)
if merchant_category == "Shopping":
    Merchant_Category = 0
elif merchant_category == "Food":
    Merchant_Category = 1
elif merchant_category == "Travel":
    Merchant_Category = 2
else:
    Merchant_Category = 3

# Device Type
device_type = st.selectbox(
    "Device Type",
    ["Mobile", "Desktop"]
)
Device_Type = 0 if device_type == "Mobile" else 1

# Transaction Device
transaction_device = st.selectbox(
    "Transaction Device",
    ["App", "Website"]
)
Transaction_Device = 0 if transaction_device == "App" else 1

# Remaining inputs (encoded numbers)
State = st.number_input("State (Encoded)", min_value=0)
City = st.number_input("City (Encoded)", min_value=0)
Bank_Branch = st.number_input("Bank Branch (Encoded)", min_value=0)
Account_Type = st.number_input("Account Type (Encoded)", min_value=0)
Transaction_Time = st.number_input("Transaction Time (Encoded)", min_value=0)
Merchant_ID = st.number_input("Merchant ID (Encoded)", min_value=0)
Transaction_Location = st.number_input("Transaction Location (Encoded)", min_value=0)
Transaction_Currency = st.number_input("Transaction Currency (Encoded)", min_value=0)
Customer_Contact = st.number_input("Customer Contact (Encoded)", min_value=0)
Transaction_Description = st.number_input("Transaction Description (Encoded)", min_value=0)
Customer_Email = st.number_input("Customer Email (Encoded)", min_value=0)

# ------------------ PREDICTION ------------------

if st.button("Predict Fraud"):

    input_data = np.array([[
        Gender, Age, State, City, Bank_Branch, Account_Type,
        Transaction_Time, Transaction_Amount, Merchant_ID,
        Transaction_Type, Merchant_Category, Account_Balance,
        Transaction_Device, Transaction_Location, Device_Type,
        Transaction_Currency, Customer_Contact,
        Transaction_Description, Customer_Email
    ]])

    result = model.predict(input_data)

    if result[0] == 1:
        st.error("Fraud Transaction Detected")
    else:
        st.success(" Normal Transaction")