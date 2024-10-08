# skills.py
import streamlit as st
from streamlit_pills import pills
import json

with open("data/technical_skills.json") as f:
    description = json.load(f)

right_column, left_column = st.columns([2, 1])

with right_column:
    st.title("Technical Skills")
    skills = list(description["skills"].keys())
    selected = pills("Select a category", skills)
with left_column:
    st.title("Description")
    st.markdown(description["skills"][selected])