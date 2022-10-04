# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ./docker-entrypoint.sh