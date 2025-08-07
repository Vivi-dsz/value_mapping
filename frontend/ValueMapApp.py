import streamlit as st
from modules.navbar import navbar 
from pages.1_welcome import welcome
from pages.2_brandanalysis import brandanalysis
from pages.3_companalysis import companalysis
from pages.4_customeranalysis import customeranalysis
from pages.5_chatbot import chatbot
from pages.6_aboutus import aboutus


def main():
    st.session_state.update(st.session_state)

    #--- Initialize session_state
    #if 'active_page' not in st.session_state:
    #    st.session_state.active_page = 'Welcome'
    #    st.session_state['chosen_brand'] = None

    # Get current values of states
    #st.session_state.active_page = st.session_state.active_page
    #st.session_state['chosen_brand'] = st.session_state['chosen_brand']

    st.set_page_config(
        page_title="Value Mapping",
        page_icon=":moneybag:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("💬 Brand Strategy Assistant")
    st.markdown("""
    Welcome to the **Value Mapping App**.

    Use the sidebar to explore:
    - Brand analysis
    - Competitive positioning
    - Customer sentiment
    - AI-driven brand strategy assistant
    """)

    navbar()
    #--- Run the active page
    if st.session_state.active_page == 'Welcome':
        welcome()
    elif st.session_state.active_page == 'Brand Analysis':
        brandanalysis()
    elif st.session_state.active_page == 'Competition Analysis':
        companalysis()
    elif st.session_state.active_page == 'Customer Analysis':
        customeranalysis()
    elif st.session_state.active_page == 'AI Chatbot':
        chatbot()
    elif st.session_state.active_page == 'About Us':
        aboutus()

if __name__ == '__main__':
    main()
