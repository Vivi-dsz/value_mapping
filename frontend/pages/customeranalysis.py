import streamlit as st
import os, sys
import pandas as pd

rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)
user_reviews_data = os.path.join(rootpath, 'data/raw/', 'user_reviews_10k_v02.csv')
user_reviews_processed_data = os.path.join(rootpath, 'data/preprocessed/', 'kw_counted_user_reviews_v01.csv')
user_reviews_sentiment_data = os.path.join(rootpath, 'data/preprocessed/', 'final_reviews_with_topics_and_sentiment.csv')

from frontend.modules.navbar import navbar
from backend.visualization.get_kw_count_df import get_kw_count_df
from backend.visualization.get_user_kw_count_df import get_user_kw_count_df
from data.raw.kw_topics_v1 import kw_dict
from data.raw.brands_about_us import brand_text
from backend.visualization.kw_count_polar_plot import kw_count_polar_plot
from backend.visualization.sentiment_heatmap import sentiment_heatmap
from backend.visualization.monthly_sentiment_plot import monthly_sentiment_plot


def customeranalysis():
    st.session_state.update(st.session_state)
    navbar()

    st.set_page_config(
        page_title="Value Mapping",
        page_icon=":moneybag:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.header("How your customers are perceiving your brand")

    left_top, gap_1, right_top = st.columns([5.5, 0.5, 4], vertical_alignment="top")

    brand_name = st.session_state['chosen_brand']

    with left_top:
        if brand_name is not None:
            df = get_kw_count_df(kw_dict, brand_text)
            df['strategy'] = df['brand']

            ### Use keyword matching (takes longer to execute on app)
            # user_reviews_df = get_user_kw_count_df(pd.read_csv(user_reviews_data), kw_dict)
            # user_reviews_df['strategy'] = 'Customer'

            ### Use already keyword matched data directly
            user_reviews_df = pd.read_csv(user_reviews_processed_data)
            user_reviews_df['strategy'] = 'Customer'

            ### Use preprocessed data with topics from model
            # user_reviews = pd.read_csv(user_reviews_sentiment_data)
            # user_reviews_df = user_reviews.groupby(['topic', 'app']).agg({'reviewId': 'count'}).reset_index().rename(columns={'topic': 'category', 'app': 'brand', 'reviewId': 'count'})
            # user_reviews_df['strategy'] = 'Customer'

            df = pd.concat([df, user_reviews_df]).reset_index(drop=True)

            fig = kw_count_polar_plot(df, kw_dict, brand_text, [brand_name], customer=True)
            st.plotly_chart(fig)
    with right_top:
        if brand_name is not None:
            st.subheader("Perception Gap Analysis")

    sentiment_data = pd.read_csv(user_reviews_sentiment_data)

    if brand_name is not None:
        st.plotly_chart(sentiment_heatmap(sentiment_data))
        st.plotly_chart(monthly_sentiment_plot(sentiment_data, brand_name))

if __name__ == '__main__':
    customeranalysis()
