FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
ENV STREAMLIT_SERVER_HEADLESS=true
CMD ["streamlit", "run", "main.py"]

