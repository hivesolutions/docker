FROM hivesolutions/alpine_dev:latest
MAINTAINER Hive Solutions

EXPOSE 22

RUN apk update && apk add openssh
RUN ssh-keygen -A
RUN adduser -D jenkins && echo "jenkins:jenkins" | chpasswd && echo "root:root" | chpasswd

CMD ["/usr/sbin/sshd", "-D"]
