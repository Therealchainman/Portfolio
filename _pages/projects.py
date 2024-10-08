# projects.py
import streamlit as st
from utils.utils import html_anchor_generator
from utils.constants import GITHUB_ICON_LINK, GITHUB_USER, GITHUB_DOMAIN

# TODO: can host these on in a database and have it connect and load from there in future.
# TODO: maybe add tech stack used in a project

class Project:
    def __init__(self, title, date, image_path, github_repo, description):
        self.username = GITHUB_USER
        self.title = title
        self.date = date
        self.image_path = image_path
        self.github_repo = github_repo
        self.description = description
    def render(self):
        st.image(self.image_path, width = 250)
        st.markdown(f"### {self.title}")
        github_link = html_anchor_generator("https://", GITHUB_DOMAIN, GITHUB_ICON_LINK, username = self.username, repo = self.github_repo)
        st.markdown(f"""
                    {self.date} &nbsp;
                    {github_link}
                    """,
                    unsafe_allow_html = True
                    )
        expander = st.expander("Read more")
        expander.write(self.description)
    def __repr__(self):
        return f"Project(title = {self.title}, image_path = {self.image_path}, github_repo = {self.github_repo}, description = {self.description})"

# json could be title -> image_path, github_repo, description
projects = [{
    "title": "Movie Reservation System",
    "date": "Sept 2024",
    "image_path": "images/movie_reservation_system.png",
    "github_repo": "movie_reservation_system",
    "description": """I'm working on this project to gain more experience with turning business logic into a fully working backend. 
               I plan to create a blogpost and video going over this project when it is complete or has more progress."""
    },
    {
    "title": "Streamlit Visualizations",
    "date": "May 2024",
    "image_path": "images/streamlit_dashboards.png",
    "github_repo": "visualizations",
    "description": """This is a project that I'm planning to continue adding to it visualizations to help solving problems in programs or business. 
               It has started with a visualization of many permutations of a directed graph with adjacency matrix representation of each graph."""
    },
    {
    "title": "Motion Prediction Pipeline",
    "date": "May 2021",
    "image_path": "images/argo_project.png",
    "github_repo": "motion_prediction_pipeline",
    "description": """This was a pet project to help me learn more about using Kubernetes, Persistent volumes, Docker and Argo workflows 
               for a machine learning task."""
    },
    {
    "title": "AI Pacman",
    "date": "May 2020",
    "image_path": "images/ai_pacman.png",
    "github_repo": "pacMan",
    "description": """School project where I implemented a Pacman game with reinforcement learning."""
    }
]

st.title("Projects")
st.markdown("----")
for data in projects:
    project = Project(**data)
    project.render()
    st.markdown("----")
