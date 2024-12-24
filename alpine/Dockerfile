FROM alpine:3.15

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

RUN apk update &&\
    apk add bash git ca-certificates python2 python3 &&\
    wget "https://bootstrap.pypa.io/get-pip.py" &&\
    wget "https://bootstrap.pypa.io/pip/2.7/get-pip.py" -O get-pip-2.py &&\
    python3 get-pip.py &&\
    python get-pip-2.py &&\
    rm get-pip.py &&\
    rm get-pip-2.py

CMD ["/bin/bash"]
