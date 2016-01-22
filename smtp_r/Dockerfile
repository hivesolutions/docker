FROM ubuntu:latest
MAINTAINER Hive Solutions

EXPOSE 25

VOLUME /data

ENV LEVEL INFO
ENV HOST 0.0.0.0
ENV PORT 25
ENV ROOT_DIR /data
ENV SMTP_AUTH memory
ENV SMTP_HOST SMTP_HOST

WORKDIR /data

RUN apt-get update && apt-get install -y -q python python-setuptools python-dev python-pip
RUN pip install --upgrade netius

CMD ["/usr/bin/python", "-m", "netius.extra.smtp_r"]
