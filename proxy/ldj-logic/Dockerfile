FROM hivesolutions/pypy:latest
MAINTAINER Hive Solutions

EXPOSE 8080

ENV LEVEL INFO
ENV HOST 0.0.0.0
ENV PORT 8080

ADD proxy.py /proxy.py

RUN pip install --upgrade netius hpack

CMD ["/usr/bin/python", "/proxy.py"]
