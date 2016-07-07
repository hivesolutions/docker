FROM hivesolutions/python:latest
MAINTAINER Hive Solutions

EXPOSE 69/udp

ENV LEVEL INFO
ENV HOST 0.0.0.0
ENV PORT 69
ENV BASE_PATH /

ADD tftpboot /tftpboot

RUN pip3 install --upgrade netius

CMD ["/usr/bin/python3", "-m", "netius.servers.tftp"]
