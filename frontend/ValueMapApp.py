import streamlit as st
from modules.navbar import navbar


def main():
    navbar()

    st.set_page_config(
        page_title="Value Mapping",
        page_icon=":moneybag:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    "# Brand Value Mapping Tool"

    """An automated brand, competitor and customer analysis serving as a fundament
    for all brand strategies - positioning, marketing, design and communication."""

    with st.popover("What is value-based brand strategy?"):
        st.markdown("Hello World 👋")

    left, center, right = st.columns(3)

    with left:
        st.subheader("Brand Analysis")

        """
        By classifying the core values your brand communicates -
        whether via advertising, website content, or product messaging -
        it becomes possible to identify and visualize the brands communicative positioning.
        """

    with center:
        st.subheader("Competitor Analysis")

        """
        Compare your brand to your competitors to find strategic competitive
        overlaps or white-space opportunities enabling data-informed brand differentiation.
        """

    with right:
        st.subheader("Target Group Analysis")

        """
        Overlay consumer value profiles with your brand’s communicative values
        to detect value misalignments or missed opportunities. This enables you
        to tailor content and messaging to resonate more deeply and enable targeted campaign planning.
        """

if __name__ == '__main__':
    main()
