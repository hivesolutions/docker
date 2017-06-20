FROM hivesolutions/python:latest
MAINTAINER Hive Solutions

EXPOSE 1080

VOLUME /data

ENV LEVEL INFO
ENV HOST 0.0.0.0
ENV PORT 1080

RUN pip3 install --upgrade netius

CMD ["/usr/bin/python3", "-m", "netius.servers.socks"]
