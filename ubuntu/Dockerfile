FROM ubuntu:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update &&\
    apt-get install -y -q --no-install-recommends bash wget git openssl ca-certificates dirmngr apt-transport-https python2 python3 python3-distutils &&\
    ln -s /usr/bin/python2 /usr/bin/python &&\
    apt-get clean && rm -rf /var/lib/apt/lists/* &&\
    wget "https://bootstrap.pypa.io/get-pip.py" &&\
    wget "https://bootstrap.pypa.io/pip/2.7/get-pip.py" -O get-pip-2.py &&\
    python3 get-pip.py &&\
    python get-pip-2.py &&\
    rm get-pip.py &&\
    rm get-pip-2.py

CMD ["/bin/bash"]
