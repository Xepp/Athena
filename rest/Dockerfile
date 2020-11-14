from python:3.8-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --quiet --no-cache-dir -r requirements.txt

COPY . /usr/src/app
