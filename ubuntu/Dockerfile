FROM ubuntu:latest
MAINTAINER Hive Solutions

RUN apt-get update &&\
    apt-get install -y bash wget git openssl ca-certificates python python3 &&\
    wget "https://bootstrap.pypa.io/get-pip.py" &&\
    python3 get-pip.py &&\
    python get-pip.py &&\
    rm get-pip.py

CMD ["/bin/bash"]
