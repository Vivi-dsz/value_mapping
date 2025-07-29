import streamlit as st
import requests
import matplotlib.pyplot as plt
import json

 # Change this URL to the one of your API
API_URL = "https://mvp-186737174934.europe-west10.run.app"

st.title("Our awesome MVP")

bank_name = st.selectbox('Which bank would you like to analyze?',
                         ("Bunq", "Revolut", "Traderepublic", "Klarna", "N26"))

url = f"{API_URL}/calculate"

params = {
    'bankname': bank_name,
}

response = requests.get(url, params=params).json()

st.write(f"This is a part of our data {float(response["pred"])}")
