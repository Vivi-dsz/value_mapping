import streamlit as st
import os, sys
import pandas as pd

rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)
review_merged_data = os.path.join(rootpath, 'data/preprocessed/', 'merged_review_topics_v01.csv')

from frontend.modules.navbar import navbar
from backend.models.agent import *
from backend.preprocess.brand_count_function import *
from backend.preprocess.review_count_function import *
from data.raw.brands_about_us import brand_text
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("OpenAI_API_KEY")

def chatbot():
    st.session_state.update(st.session_state)
    navbar()

    st.set_page_config(
        page_title="Value Mapping",
        page_icon=":moneybag:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    review_merged_df = pd.read_csv(review_merged_data)

    @st.cache_data
    def load_keyword_dfs():
        brand_kw_df = get_brand_counts(brand_text, keywords)
        review_kw_df = get_review_counts(review_merged_df, keywords)
        return brand_kw_df, review_kw_df

    brand_kw_df, review_kw_df = load_keyword_dfs()

    # Streamlit app setup
    st.title("💬 Brand Strategy Assistant")
    st.caption("🚀 A brand expert chatbot powered by OpenAI")
    st.markdown("""I analyze brand perception, user sentiment, and market positioning
                to support your strategy. Just name a brand or challenge —
                I’ll start with a quick diagnosis and offer more detail if needed.
                """)

    left, center, right = st.columns([4,4,4], vertical_alignment="top")
    with left:
        openai_api_key = st.text_input("Please Provide an OpenAI API Key to continue:", key="chatbot_api_key", type="password")

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
            api_key=openai_api_key,
            chat_history=st.session_state.messages,
            last_brands=st.session_state.last_brands
            )

        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)


if __name__ == '__main__':
    chatbot()
