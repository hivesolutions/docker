FROM hivesolutions/alpine_dev:latest
MAINTAINER Hive Solutions

EXPOSE 22

RUN apk update && apk add openssh openjdk7
RUN ssh-keygen -A
RUN adduser -D jenkins && echo "jenkins:jenkins" | chpasswd

CMD ["/usr/sbin/sshd", "-D"]
