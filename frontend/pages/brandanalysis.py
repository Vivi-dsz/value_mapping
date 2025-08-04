import streamlit as st
import os, sys

rootpath = os.path.join(os.getcwd(), '..')
sys.path.append(rootpath)

from frontend.modules.navbar import navbar
from frontend.modules.companydesc import companydesc
from backend.visualization.get_kw_count_df import get_kw_count_df
from data.raw.kw_topics_v1 import kw_dict
from data.raw.brands_about_us import brand_text
from backend.visualization.kw_count_polar_plot import kw_count_polar_plot

def main():
    navbar()

    st.set_page_config(
        page_title="Value Mapping",
        page_icon=":moneybag:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.header("Analyse your company")

    left_top, gap, right_top, gap_2 = st.columns([2, 1, 4, 1], vertical_alignment="top")

    with left_top:
        brand_name = st.selectbox('Which company would you like to analyze?',
                                ("Bunq", "Revolut", "Trade Republic", "Klarna", "N26"),
                                index=None, placeholder="Choose your company")

    with right_top:
        if brand_name is not None:
            st.write(companydesc[brand_name])

    st.subheader("Your brand's positioning")

    left_bottom, gap_3, right_bottom, gap_4 = st.columns([4, 1, 4, 1], vertical_alignment="top")

    with left_bottom:
        if brand_name is not None:
            df = get_kw_count_df(kw_dict, brand_text)

            brand_name_list = []
            brand_name_list.append(brand_name)

            fig = kw_count_polar_plot(df, kw_dict, brand_text, brand_name_list=brand_name_list)

            st.plotly_chart(fig)

    with right_bottom:
        if brand_name is not None:
            st.write("Analysis of brand's positioning")

            selected_df = df[df['brand'] == brand_name].reset_index(drop=True)

            st.dataframe(selected_df.groupby(['category', 'keyword']).agg({'count':'sum'}))

if __name__ == '__main__':
    main()
