FROM hivesolutions/alpine:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

ENV LD_LIBRARY_PATH "/opt/lib:/usr/local/lib:/usr/lib:/lib"
ENV LIBRARY_PATH "/opt/lib:/usr/local/lib:/usr/lib:/lib"
ENV PATH "/opt/bin:/usr/local/bin:/usr/bin:/bin"
ENV PYTHON2_VERSION "2.7.18"

RUN apk update && apk add sudo gcc make linux-headers libc-dev openssl-dev python3-dev zlib-dev jpeg-dev &&\
    wget https://www.python.org/ftp/python/${PYTHON2_VERSION}/Python-${PYTHON2_VERSION}.tgz &&\
    tar -xvzf Python-${PYTHON2_VERSION}.tgz &&\
    cd Python-${PYTHON2_VERSION} &&\
    ./configure &&\
    make &&\
    make install &&\
    cd .. && \
    rm -rf Python-${PYTHON2_VERSION} &&\
    rm Python-${PYTHON2_VERSION}.tgz &&\
    wget "https://bootstrap.pypa.io/pip/2.7/get-pip.py" -O get-pip-2.py &&\
    python2 get-pip-2.py &&\
    rm get-pip-2.py

CMD ["/bin/bash"]
