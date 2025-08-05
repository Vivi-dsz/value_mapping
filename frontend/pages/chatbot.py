import streamlit as st
from modules.navbar import navbar


def chatbot():
    st.session_state.update(st.session_state)
    navbar()

    st.set_page_config(
        page_title="Value Mapping",
        page_icon=":moneybag:",
        layout="wide",
        initial_sidebar_state="expanded"
    )


import pandas as pd
import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from backend.models.agent import *
from backend.preprocess.brand_count_function import *
from backend.preprocess.review_count_function import *
from data.preprocessed.dataframes import review_merged_df
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

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
st.markdown("""
I analyze brand perception, user sentiment, and market positioning to support your strategy. Just name a brand or challenge — I’ll start with a quick diagnosis and offer more detail if needed."""
            )

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


if __name__ == '__main__':
    chatbot()
