FROM hivesolutions/python:latest
MAINTAINER Hive Solutions

EXPOSE 8080

VOLUME /data/letsencrypt

ENV LEVEL INFO
ENV HOST 0.0.0.0
ENV PORT 8080
ENV SAFE 0
ENV CHILDREN 0
ENV ECHO 1

ADD proxy.py /proxy.py

RUN pip3 install --upgrade netius hpack

CMD ["/usr/bin/python3", "/proxy.py"]
