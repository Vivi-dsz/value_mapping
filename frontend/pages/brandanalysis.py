import streamlit as st
import os, sys
import pandas as pd

#rootpath = os.path.join(os.getcwd(), '..')
#sys.path.append(rootpath)

#brand_processed_data = os.path.join('../lemmatized_brand_kw_count.csv')

from modules.navbar import navbar
from modules.companydesc import companydesc
from modules.brandinfo import brand_analysis_info
from data.raw.kw_topics_v1 import kw_dict
from data.raw.brands_about_us import brand_text
from backend.visualization.kw_count_polar_plot import kw_count_polar_plot

def refresh_competitors():
    brand_name = st.session_state['chosen_brand']
    allbrands = ["Bunq", "Revolut", "Trade Republic", "Klarna", "N26"]
    competitors = [x for x in allbrands if x != brand_name]
    st.session_state['chosen_competitors'] = competitors

def brandanalysis():
    st.session_state.update(st.session_state)

    navbar()

    st.set_page_config(
        page_title="Value Mapping",
        page_icon=":moneybag:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.header("Analyse your company")

    left_top, gap, right_top, gap_2 = st.columns([3, 1, 4, 1], vertical_alignment="top")

    with left_top:
        brand_name = st.selectbox('Which company would you like to analyze?', key='chosen_brand',
                                options=("Bunq", "Revolut", "Trade Republic", "Klarna", "N26"),
                                index=None, placeholder="Choose your company",
                                on_change=refresh_competitors)

    with right_top:
        if brand_name is not None:
            st.write(companydesc[brand_name])

    st.subheader("Your brand's positioning")

    left_bottom, gap_3, right_bottom = st.columns([5, 0.5, 4.5], vertical_alignment="top")

    with left_bottom:
        if brand_name is not None:

            df = pd.read_csv('./pages/lemmatized_brand_kw_count.csv')

            brand_name_list = []
            brand_name_list.append(brand_name)

            fig = kw_count_polar_plot(df, kw_dict, brand_text, brand_name_list=brand_name_list)

            st.plotly_chart(fig)

    with right_bottom:
        if brand_name is not None:
            st.subheader("Analysis of brand's positioning")

            #selected_df = df[df['brand'] == brand_name].reset_index(drop=True)
            #pivot_table = selected_df.pivot_table(values='count', index=['category', 'keyword'], columns='brand', aggfunc='sum')
            #pivot_table[pivot_table.columns] = pivot_table[pivot_table.columns].fillna(0).astype(int)
            #st.dataframe(pivot_table)

            st.markdown(brand_analysis_info[brand_name])

if __name__ == '__main__':
    brandanalysis()
