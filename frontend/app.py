import streamlit as st
import requests
import matplotlib.pyplot as plt
import json

 # Change this URL to the one of your API
API_URL = "https://mvp-186737174934.europe-west10.run.app"

st.title("Our awesome MVP")

url = f"{API_URL}/predict"

with st.form("predict"):
    bank_name = st.selectbox('Which bank are you using?',
                             ("Bunq", "Revolut", "Traderepublic", "Klarna", "N26"))
    user_review = st.text_input("Please write your review")
    submit = st.form_submit_button("Predict 🚀")

if submit:
    params = {
        'bankname': bank_name,
        'user_review': user_review,
    }
    response = requests.get(url, params=params).json()#
    topic = response['prediction']
    st.success(f"Predicted Review Topic **{topic}**")


#### Following code is for using with the dummy.py function
#### to show the API can read csv file in the data folder
# bank_name = st.selectbox('Which bank would you like to analyze?',
#                          ("Bunq", "Revolut", "Traderepublic", "Klarna", "N26"))
# url = f"{API_URL}/calculate"
# params = {
#     'bankname': bank_name,
# }
# response = requests.get(url, params=params).json()
# st.write(f"This is a part of our data {float(response["pred"])}")
