# main.py
import streamlit as st
from utils.utils import html_anchor_generator
from utils.constants import GITHUB_ICON_LINK, LINKEDIN_ICON_LINK, GMAIL_ICON_LINK, GITHUB_USER, LINKEDIN_USER, GMAIL_ADDRESS, GITHUB_DOMAIN, LINKEDIN_DOMAIN

st.sidebar.markdown(
    f"""
    <div style='text-align: center;'>
    {html_anchor_generator('https://', LINKEDIN_DOMAIN, LINKEDIN_ICON_LINK, username = LINKEDIN_USER)}
    &nbsp;&nbsp;&nbsp;&nbsp;
    {html_anchor_generator('https://', GITHUB_DOMAIN, GITHUB_ICON_LINK, username = GITHUB_USER)}
    &nbsp;&nbsp;&nbsp;&nbsp;
    {html_anchor_generator('mailto:', {GMAIL_ADDRESS}, GMAIL_ICON_LINK)}
    </div>
    """, 
    unsafe_allow_html = True
)

directory = "_pages/"

pages = [st.Page(f"{directory}about.py", title = "Home", icon = "👋"),
        st.Page(f"{directory}experience.py", title = "Experience", icon = "🏢"), st.Page(f"{directory}projects.py", title = "Projects", icon = "📈"), 
        st.Page(f"{directory}skills.py", title = "Technical Skills", icon = "🧰"), st.Page(f"{directory}education.py", title = "Education", icon = "🏫"), 
        st.Page(f"{directory}blog.py", title = "Blog", icon = "✍️"), st.Page(f"{directory}contact.py", title = "Contact", icon = "📧")]
pg = st.navigation(pages)
pg.run()

