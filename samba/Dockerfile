FROM alpine:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 137
EXPOSE 138
EXPOSE 139
EXPOSE 445

VOLUME /data

ENV USERNAME samba
ENV PASSWORD password
ENV WORKGROUP WORKGROUP
ENV ENCRYPTION auto
ENV SIGNING auto

ADD run.sh /run.sh

RUN apk update &&\
    apk add --no-cache samba samba-common-tools

ADD smb.conf /etc/samba/smb.conf

CMD ["/run.sh"]
