# education.py
import streamlit as st

st.title("Education")

st.markdown("----")

st.image("images/Cal_logo.png", width = 200)
st.markdown("### Bachelor Degree")
st.markdown("May 2017 - May 2020")
expander = st.expander("Read more")
expander.write("""
               I hold a Bachelor's degree from the University of California, Berkeley, where I majored in 
               Physics and Applied Mathematics, with additional coursework in Computer Science.
               """)

st.markdown("----")