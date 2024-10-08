# Welcome to my portfolio web app

This is a simple web app that I created to showcase my projects and skills. It is built using the python library streamlit, that is used for creating dashboards, and interactive visualizations. 

## Running locally

This was built on linux operating system with docker version 24.0.7, and docker-compose version 1.29.2.

This can be ran using docker compose, with the `docker-compose.yaml` files. 

Run this part to build it from the Dockerfile

```sh
docker-compose build
```

Then you can run this part to start the container
    
```sh
docker-compose up
```

And now you can make changes to the python files and it will update to the web app running in a docker container because it is mounting the local directory to the container.

Then publishing to docker hub is as simple as running this command

```sh
docker push <dockerhub_username>/portfolio-web-app:latest
```

These is what I use to run it locally without docker using a virtual environment. 

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```