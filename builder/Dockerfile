FROM hivesolutions/alpine_dev:latest
MAINTAINER Hive Solutions

VOLUME /repo

ENV NAME ""
ENV EXEC "Dockerfile"
ENV BUILDER "Dockerfile"

ADD run.sh /run.sh

WORKDIR /repo

RUN apk install docker

CMD ["/run.sh"]
