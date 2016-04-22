FROM hivesolutions/alpine_dev:latest
MAINTAINER Hive Solutions

EXPOSE 22

ENV LD_LIBRARY_PATH "/opt/lib:/usr/local/lib:/usr/lib:/lib"
ENV LIBRARY_PATH "/opt/lib:/usr/local/lib:/usr/lib:/lib"

RUN apk update && apk add openssh openjdk7
RUN ssh-keygen -A
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN adduser -D jenkins && (echo "jenkins:jenkins" | chpasswd) && (echo "root:root" | chpasswd)

CMD ["/usr/sbin/sshd", "-D"]
