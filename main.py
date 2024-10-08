# main.py
import streamlit as st
from utils.utils import html_anchor_generator
from utils.constants import GITHUB_ICON_LINK, LINKEDIN_ICON_LINK, GMAIL_ICON_LINK, GITHUB_USER, LINKEDIN_USER, GMAIL_ADDRESS, GITHUB_DOMAIN, LINKEDIN_DOMAIN

st.sidebar.markdown(
    f"""
    <div style='text-align: center;'>
    {html_anchor_generator(LINKEDIN_DOMAIN, LINKEDIN_ICON_LINK, username = LINKEDIN_USER)}
    &nbsp;&nbsp;&nbsp;&nbsp;
    {html_anchor_generator(GITHUB_DOMAIN, GITHUB_ICON_LINK, username = GITHUB_USER)}
    &nbsp;&nbsp;&nbsp;&nbsp;
    {html_anchor_generator(f'mailto:{GMAIL_ADDRESS}', GMAIL_ICON_LINK)}
    </div>
    """, 
    unsafe_allow_html = True
)

pages = [st.Page("_pages/about.py", title = "Home", icon = "👋"),
        st.Page("_pages/experience.py", title = "Experience", icon = "🏢"), st.Page("_pages/projects.py", title = "Projects", icon = "📈"), 
        st.Page("_pages/skills.py", title = "Technical Skills", icon = "🧰"), st.Page("_pages/education.py", title = "Education", icon = "🏫"), 
        st.Page("_pages/blog.py", title = "Blog", icon = "✍️"), st.Page("_pages/contact.py", title = "Contact", icon = "📧")]
pg = st.navigation(pages)
pg.run()

