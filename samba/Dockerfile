FROM hivesolutions/alpine:latest
MAINTAINER Hive Solutions

EXPOSE 8080

VOLUME /data

ENV PASSWORD password

ADD smb.conf /etc/samba/smb.conf
ADD run.sh /run.sh

RUN apk update &&\
    apk add samba samba-common-tools

CMD ["/usr/sbin/smbd", "-FS"]
