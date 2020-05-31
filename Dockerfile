FROM python:3.8.3-alpine3.11
COPY src /src
WORKDIR src
RUN pip install -r requirements.txt