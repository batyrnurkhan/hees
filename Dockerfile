FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /hees

WORKDIR /hees

ADD . /hees/

EXPOSE 8000

RUN pip install -r requirements.txt
