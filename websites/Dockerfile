FROM ubuntu:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV SERVER_ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080

RUN apt-get update && apt-get install -y -q python python-setuptools python-dev python-pip git
RUN git clone https://hive_development:4mBSDQdQzTW4NvmJ@bitbucket.org/hivesolutions/websites.git
RUN pip install -r /websites/requirements.txt && pip install --upgrade netius

CMD python /websites/src/default/main.py
