FROM hivesolutions/python:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV HOST 0.0.0.0
ENV PORT 8080

WORKDIR /data

RUN pip3 install --upgrade netius

CMD ["/usr/bin/python3", "-m", "netius.extra.proxy_d"]
