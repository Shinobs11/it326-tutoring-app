# syntax=docker/dockerfile:1
FROM python:bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt ./
COPY docker-entrypoint.sh ./
COPY wait-for-it.sh ./

RUN pip install -r requirements.txt




ENV PORT 8000
EXPOSE 8000

USER root
RUN ["chmod", "+x" ,"./docker-entrypoint.sh"]
RUN ["chmod", "+x", "./wait-for-it.sh"]
# ENTRYPOINT ./docker-entrypoint.sh