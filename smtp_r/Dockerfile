FROM hivesolutions/python:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 25

VOLUME /data

ENV LEVEL INFO
ENV HOST 0.0.0.0
ENV PORT 25
ENV ROOT_DIR /data
ENV SMTP_AUTH memory
ENV SMTP_HOST SMTP_HOST

WORKDIR /data

RUN pip3 install --upgrade netius logstash-api

CMD ["/usr/bin/python3", "-m", "netius.extra.smtp_r"]
