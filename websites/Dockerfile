FROM ubuntu:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV HOST 0.0.0.0
ENV PORT 8080

ADD requirements.txt /

RUN apt-get update && apt-get install -y -q python python-setuptools python-dev python-pip
RUN pip install -r /requirements.txt && pip install --upgrade netius
RUN git clone https://hive_development:4mBSDQdQzTW4NvmJ@bitbucket.org/hivesolutions/websites.git src

CMD python /src/default/main.py
