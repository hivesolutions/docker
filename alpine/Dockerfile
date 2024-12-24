FROM alpine:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

ENV PIP_BREAK_SYSTEM_PACKAGES "1"

RUN apk update &&\
    apk add bash git ca-certificates python3 &&\
    wget "https://bootstrap.pypa.io/get-pip.py" &&\
    python3 get-pip.py &&\
    rm get-pip.py

CMD ["/bin/bash"]
