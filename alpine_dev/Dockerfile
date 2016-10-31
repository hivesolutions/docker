FROM hivesolutions/alpine:latest
MAINTAINER Hive Solutions

ENV LD_LIBRARY_PATH "/opt/lib:/usr/local/lib:/usr/lib:/lib"
ENV LIBRARY_PATH "/opt/lib:/usr/local/lib:/usr/lib:/lib"

RUN apk update && apk add sudo gcc make linux-headers libc-dev python-dev python3-dev 

CMD ["/bin/bash"]
