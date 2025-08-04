import streamlit as st
from modules.navbar import navbar


def welcome():
    st.session_state.update(st.session_state)
    navbar()

    st.set_page_config(
        page_title="Value Mapping",
        page_icon=":moneybag:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Brand Value Mapping Tool")

    st.markdown("""An automated brand, competitor and customer analysis serving as a fundament
    for all brand strategies - positioning, marketing, design and communication.""")

    with st.popover("What is value-based brand strategy?"):
        st.markdown("""Building a brand's identity, messaging, and positioning
                    around the core human values it communicates. Instead of
                    focusing solely on product features or visual identity, it asks:
                    *What does this brand stand for? What deeper motivations does it
                    connect with in people's lives?* By aligning brand communication
                    with the values that resonate most with target audiences,
                    companies can create stronger emotional bonds, stand out in
                    competitive markets, and build more consistent, meaningful brand
                    experiences across all touchpoints.""")

    left, center, right = st.columns(3)

    with left:
        st.subheader("Brand Analysis")

        st.markdown("""
        By classifying the core values your brand communicates -
        whether via advertising, website content, or product messaging -
        it becomes possible to identify and visualize the brands communicative positioning.
        """)

    with center:
        st.subheader("Competitor Analysis")

        st.markdown("""
        Compare your brand to your competitors to find strategic competitive
        overlaps or white-space opportunities enabling data-informed brand differentiation.
        """)

    with right:
        st.subheader("Target Group Analysis")

        st.markdown("""
        Overlay consumer value profiles with your brand’s communicative values
        to detect value misalignments or missed opportunities. This enables you
        to tailor content and messaging to resonate more deeply and enable targeted campaign planning.
        """)

if __name__ == '__main__':
    welcome()
