FROM ubuntu:rolling
MAINTAINER Hive Solutions

RUN apt-get update &&\
    apt-get install -y -q bash wget git openssl ca-certificates apt-transport-https python python3 &&\
    wget "https://bootstrap.pypa.io/get-pip.py" &&\
    python3 get-pip.py &&\
    python get-pip.py &&\
    rm get-pip.py

CMD ["/bin/bash"]
