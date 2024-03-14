FROM python:3.11.6-alpine3.18

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update && apk add bash

COPY . ./srv

RUN cd srv/ && pip install -r requirements.txt