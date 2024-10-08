# main.py
import streamlit as st
from utils import html_anchor_generator
from constants import GITHUB_ICON_LINK, LINKEDIN_ICON_LINK, GMAIL_ICON_LINK, GITHUB_USER, LINKEDIN_USER, GMAIL_ADDRESS, GITHUB_DOMAIN, LINKEDIN_DOMAIN

st.sidebar.markdown(
    f"""
    <div style='text-align: center;'>
    {html_anchor_generator(LINKEDIN_DOMAIN, LINKEDIN_ICON_LINK, username = LINKEDIN_USER)}
    &nbsp;&nbsp;&nbsp;&nbsp;
    {html_anchor_generator(GITHUB_DOMAIN, GITHUB_ICON_LINK, username = GITHUB_USER)}
    &nbsp;&nbsp;&nbsp;&nbsp;
    {html_anchor_generator(GMAIL_ADDRESS, GMAIL_ICON_LINK)}
    </div>
    """, 
    unsafe_allow_html = True
)

pages = [st.Page("about.py", title = "Home", icon = "👋"),
        st.Page("experience.py", title = "Experience", icon = "🏢"), st.Page("projects.py", title = "Projects", icon = "📈"), 
        st.Page("skills.py", title = "Technical Skills", icon = "🧰"), st.Page("education.py", title = "Education", icon = "🏫"), 
        st.Page("blog.py", title = "Blog", icon = "✍️"), st.Page("contact.py", title = "Contact", icon = "📧")]
pg = st.navigation(pages)
pg.run()

