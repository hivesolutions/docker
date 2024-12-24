FROM alpine:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

RUN apk update &&\
    apk add bash git ca-certificates python2 python3 &&\
    wget "https://bootstrap.pypa.io/get-pip.py" &&\
    python3 get-pip.py &&\
    rm get-pip.py

CMD ["/bin/bash"]
