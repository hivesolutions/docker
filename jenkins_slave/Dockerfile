FROM hivesolutions/alpine_devlatest
MAINTAINER Hive Solutions

EXPOSE 22

RUN apk update && apk add openssh
RUN adduser -D jenkins && echo "jenkins:jenkins" | chpasswd

CMD ["/usr/sbin/sshd", "-D"]
