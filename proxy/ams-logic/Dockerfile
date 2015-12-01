FROM ubuntu:latest
MAINTAINER Hive Solutions

EXPOSE 80

ENV LEVEL INFO
ENV HOST 0.0.0.0
ENV PORT 80

ADD proxy.py /proxy.py

RUN apt-get update && apt-get install -y -q python python-setuptools python-dev python-pip
RUN pip install --upgrade netius

CMD python /proxy.py
