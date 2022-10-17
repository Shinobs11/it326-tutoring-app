# syntax=docker/dockerfile:1
FROM python:bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./



ENV PORT 8000
EXPOSE 8000

RUN ["chmod", "+x" ,"./docker-entrypoint.sh"]
# ENTRYPOINT ./docker-entrypoint.sh