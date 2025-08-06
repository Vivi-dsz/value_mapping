import streamlit as st

st.set_page_config(page_title="About Us", layout="centered")

st.title("About Our Leadership Team")
st.markdown("Meet the creators behind the Brand Strategy AI Assistant")

# Team Members
team = [
    {
        "title": "Chief Executive Officer (CEO)",
        "name": "Vivien Daszkowski",
        "image": "",
        "In-Project Role": "Founder of the core idea, led the presentation, and established the main workflows for the team.",
        "Real-World Role":
        """Before joining the bootcamp, Vivien did her Master’s degree in Management and worked at the intersection of business and tech - as Managing Director of a spin-off of a strategy consultancy.
        She learned to code and deepen her technical skills to contribute more effectively to data-driven decision-making and product development.""",
        "github": "https://github.com/Vivi-dsz",
        "linkedin": "https://www.linkedin.com/in/vivien-daszkowski/"
    },
    {
        "title": "Chief Product Officer (CPO)",
        "name": "Liana Gilmanova",
        "image": "",
        "In-Project Role": "Focused on product development — created the system diagram and proposed the initial MVP structure.",
        "Real-World Role":
        """Liana is a Product Manager with 8 years experience in building and scaling Customer facing Products across 18 countries
        and complex cross-functional teams. As data and AI increasingly shape product strategy, she is now expanding her skillset
        to better lead the development of data-driven and AI-powered products.""",
        "github": "https://github.com/gilmali",
        "linkedin": "https://www.linkedin.com/in/ligilmanova/"
    },
    {
        "title": "Chief Technology Officer (CTO)",
        "name": "Ibrahim Eksi",
        "image": "",
        "In-Project Role": "Owns the scraping pipeline setup, fronend, and supports the broader technical infrastructure.",
        "Real-World Role":
        """Mechanical engineer with experience in vehicle simulations. After 2+ years of working in data analysis,
        he now develops new skills to continue his career as a data scientist.""",
        "github": "https://github.com/ibraeksi",
        "linkedin": "https://www.linkedin.com/in/ibrahim-eksi/"
    },
    {
        "title": "Chief Innovation Officer (CIO)",
        "name": "Dr. Elnaz Roshan",
        "image": "",
        "In-Project Role": "Responsible for the AI model development and integration, ensuring metrics and functions are practical and intelligent.",
        "Real-World Role":
        """Elnaz holds a Ph.D. in Climate Economics with 10+ years of experience in evaluating climate policies and risks across sectors,
        applying quantitative and analytical forward-looking optimization modeling, and leading small teams.
        Currently diving into data science to strengthen her technical skills further and support impactful sustainability solutions.""",
        "github": "https://github.com/elnroshan",
        "linkedin": "https://www.linkedin.com/in/elnaz-roshan/"
    },

]

# Layout
for member in team:
    cols = st.columns([1, 3])
    with cols[0]:
        st.image(member["image"], width=120)
    with cols[1]:
        st.subheader(member["name"])
        st.caption(member["title"])
        st.write(member["In-Project Role"])
        st.write(member["Real-World Role"])
        st.markdown(f"[GitHub]({member['github']}) | [LinkedIn]({member['linkedin']})")
    st.markdown("---")

import streamlit as st
