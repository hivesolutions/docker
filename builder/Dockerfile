FROM hivesolutions/alpine_dev:latest
MAINTAINER Hive Solutions

VOLUME /repo
VOLUME /var/run/docker.sock

USER root

ENV NAME ""
ENV EXEC "/"
ENV BUILDER "Dockerfile"
ENV REPO "docker.stage.hive.pt"

ADD run.sh /run.sh

WORKDIR /repo

RUN apk add docker
RUN mkdir -p /var/run

CMD ["/run.sh"]
