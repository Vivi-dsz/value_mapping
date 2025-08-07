import streamlit as st

st.set_page_config(page_title="About Us", layout="wide")

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
        """Vivien did her Master’s degree in Management and worked at the intersection of business and tech
        - as Managing Director of a spin-off of a strategy consultancy.""",
        "github": "https://github.com/Vivi-dsz",
        "linkedin": "https://www.linkedin.com/in/vivien-daszkowski/"
    },
    {
        "title": "Chief Technology Officer (CTO)",
        "name": "Ibrahim Eksi",
        "image": "",
        "In-Project Role": "Owns the scraping pipeline setup, fronend, and supports the broader technical infrastructure.",
        "Real-World Role":
        """Ibrahim is a Mechanical Engineer with experience in vehicle simulations with 2+ years experience in data analysis.""",
        "github": "https://github.com/ibraeksi",
        "linkedin": "https://www.linkedin.com/in/ibrahim-eksi/"
    },
    {
        "title": "Chief Product Officer (CPO)",
        "name": "Liana Gilmanova",
        "image": "",
        "In-Project Role": "Focused on product development — created the system diagram and proposed the initial MVP structure.",
        "Real-World Role":
        """Liana is a Product Manager with 8 years experience in building and scaling Customer facing Products across 18 countries
        and complex cross-functional teams.""",
        "github": "https://github.com/gilmali",
        "linkedin": "https://www.linkedin.com/in/ligilmanova/"
    },
    {
        "title": "Chief Innovation Officer (CIO)",
        "name": "Elnaz Roshan, Ph.D.",
        "image": "",
        "In-Project Role": "Responsible for the AI model development and integration, ensuring metrics and functions are practical and intelligent.",
        "Real-World Role":
        """Elnaz is a Climate Economics with 10+ years of experience in evaluating climate transition
        forward-looking optimization modeling, and leading small teams.""",
        "github": "https://github.com/elnroshan",
        "linkedin": "https://www.linkedin.com/in/elnaz-roshan/"
    },

]

# Layout 2x2
def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Display in 2x2 layout
for row in chunk_list(team, 2):
    cols = st.columns(2)
    for idx, member in enumerate(row):
        with cols[idx]:
            #st.image(member["image"], width=150)
            st.markdown(f"## {member['name']}")
            st.caption(member["title"])

            st.markdown("**In-Project Role**")
            st.write(member["In-Project Role"])

            st.markdown("**Real-World Role**")
            st.write(member["Real-World Role"])

            st.markdown(f"[GitHub]({member['github']}) | [LinkedIn]({member['linkedin']})")

# Layout Nx1
# for member in team:
#     cols = st.columns([1, 3])
#     with cols[0]:
#         pass  # st.image(member["image"], width=120)
#     with cols[1]:
#         st.subheader(member["name"])
#         st.caption(member["title"])

#         # Add bold labels for roles
#         st.markdown("**In-Project Role**")
#         st.write(member["In-Project Role"])

#         st.markdown("**Real-World Role**")
#         st.write(member["Real-World Role"])

#         st.markdown(f"[GitHub]({member['github']}) | [LinkedIn]({member['linkedin']})")

#     st.markdown("---")
