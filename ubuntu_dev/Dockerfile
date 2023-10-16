FROM hivesolutions/ubuntu:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update &&\
    apt-get install -y -q --no-install-recommends sudo gcc make curl pypy linux-headers-generic\
    libssl-dev python2-dev python3-dev pypy-dev &&\
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
