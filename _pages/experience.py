# experience.py
import streamlit as st

st.title("Experience")

st.markdown("----")

st.image("images/gm.png", width = 250)
st.markdown("## Software Engineer")
st.markdown("Jul 2020 - Aug 2024")

st.markdown("### Map Creation for Super Cruise")
expander = st.expander("Read more")
expander.markdown("Worked on a team that creates maps for Super Cruise, an advanced driver-assistance system (ADAS) that offers hands-free driving on compatible highways.")
expander.markdown("I worked on many data engineering products at big data scale for the map creation pipeline")
expander.markdown("Languages: Python, SQL, Scala")
expander.markdown("Technology:  distributed Computing, big data, Apache Spark, Databricks, Azure Synapse Analytics, AWS S3, Azure Data Lake Storage, postgreSQL, Geospatial data, Geojson, XML, Json, Parquet, ORC, Hadoop, Hive, Mlflow, Docker, Kubernetes, Delta Table, Github, Jira")
expander.image("images/hd_map.png", width = 400)

st.markdown("### HPC Infrastructure for AIML")
expander = st.expander("Read more")
expander.markdown("Worked on a team that provides HPC+ infrastructure for AIML.  Specific tasks were related to working on kubernetes and setting up Argo and other machine learning tools on the kubernetes cluster.")
expander.markdown("Languages: Python, Go")
expander.markdown("Technology: Linux, Kubernetes, Ray, Apache Spark, Argo, Helm, Docker, protocol buffers")
st.markdown("----")

