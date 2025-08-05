import pandas as pd
import os, sys

rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)

from backend.models.agent import *
from backend.preprocess.brand_count_function import *
from backend.preprocess.review_count_function import *
from data.preprocessed.dataframes import review_merged_df
import streamlit as st
from dotenv import load_dotenv

api_key = os.getenv("OpenAI_API_KEY")

@st.cache_data
def load_keyword_dfs():
    brand_kw_df = get_brand_counts(brand_text, keywords)
    review_kw_df = get_review_counts(review_merged_df, keywords)
    return brand_kw_df, review_kw_df

brand_kw_df, review_kw_df = load_keyword_dfs()

# Streamlit app setup
st.title("💬 Brand Strategy Assisstant")
st.caption("🚀 A brand expert chatbot powered by OpenAI")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state["messages"] = [{"role": "assistant", "content": "Ready to shape your next branding move?"}]

if "last_brands" not in st.session_state:
    st.session_state.last_brands = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # Call your custom agent
    msg = handle_query(
        question = prompt,
        brand_kw_df=brand_kw_df,
        review_kw_df=review_kw_df,
        api_key=api_key,
        chat_history=st.session_state.messages,
        last_brands=st.session_state.last_brands
        )

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
