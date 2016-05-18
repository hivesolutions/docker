FROM hivesolutions/alpine_dev:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV HOST 0.0.0.0
ENV PORT 8080

ADD proxy.py /proxy.py

RUN pip3 install --upgrade netius

CMD ["/usr/bin/python3", "/proxy.py"]
