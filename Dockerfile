FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /hees

WORKDIR /hees

ADD . /hees/

RUN pip install -r requirements.txt