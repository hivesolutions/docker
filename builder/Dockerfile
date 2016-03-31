FROM hivesolutions/alpine_dev:latest
MAINTAINER Hive Solutions

VOLUME /repo

ENV NAME ""
ENV EXEC ""
ENV BUILDER "Dockerfile"

ADD run.sh /run.sh

WORKDIR /repo

RUN apk add docker

CMD ["/run.sh"]
