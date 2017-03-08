FROM hivesolutions/alpine:latest
MAINTAINER Hive Solutions

EXPOSE 8080

VOLUME /data

RUN apk update &&\
    apk add samba samba-common-tools

CMD ["smbd"]
