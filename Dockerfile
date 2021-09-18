FROM docker.io/python:3.9-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT gunicorn -b 0.0.0.0:8000 app:app
