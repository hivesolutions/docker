FROM hivesolutions/alpine:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

ENV LD_LIBRARY_PATH "/opt/lib:/usr/local/lib:/usr/lib:/lib"
ENV LIBRARY_PATH "/opt/lib:/usr/local/lib:/usr/lib:/lib"

RUN apk update && apk add sudo gcc make linux-headers libc-dev openssl-dev python2-dev python3-dev zlib-dev jpeg-dev

CMD ["/bin/bash"]
