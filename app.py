import streamlit as st
import pandas as pd
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit App
st.title("Churn Prediction App")

# Sidebar for user input
st.sidebar.header("User Input")

subscription_months = st.sidebar.slider("Subscription Months", 1, 24, 12)
monthly_bill = st.sidebar.slider("Monthly Bill", 30.0, 100.0, 50.0)
total_usage_gb = st.sidebar.slider("Total Usage GB", 100, 500, 250)
usage_subcription = st.sidebar.slider("Usage",1,500)
monthly_usage = st.sidebar.slider("Monthly Usage",10,200,20)
total_amount_paid = st.sidebar.slider("Total Amount Paid", 100,2000,50)
# Create feature vector
features = [[ subscription_months, monthly_bill, total_usage_gb,usage_subcription]]

# Make predictions
prediction = model.predict(features)

# Display prediction
st.subheader("Prediction")
if prediction[0] == 0:
    st.write("The customer is likely to stay.")
else:
    st.write("The customer is likely to churn.")

