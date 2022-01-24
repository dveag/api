FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /backend
WORKDIR /backend

ADD ./requirements.txt .

RUN pip3 install -r requirements.txt

USER 1000:1000

WORKDIR /backend/nftapi
