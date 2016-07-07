FROM hivesolutions/python:latest
MAINTAINER Hive Solutions

VOLUME /repo

USER root

ENV NAME ""
ENV EXEC "/"
ENV BUILDER "Dockerfile"
ENV REPO "docker.stage.hive.pt"

ADD run.sh /run.sh

WORKDIR /repo

RUN apk add docker

CMD ["/run.sh"]
