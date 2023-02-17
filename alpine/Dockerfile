FROM alpine:3.17

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

RUN apk update &&\
    apk add bash git ca-certificates python3 &&\
    wget "https://bootstrap.pypa.io/get-pip.py" &&\
    python3 get-pip.py &&\
    rm get-pip.py

COPY bin-python.patch /root/bin-python.patch
RUN apk add --virtual .alpine-sdk alpine-sdk &&\
    git clone --depth 1 --branch v3.15.7 git://git.alpinelinux.org/aports ~/aports &&\
    git -C ~/aports apply ~/bin-python.patch &&\
    cd ~/aports/community/python2 && abuild-keygen -a -n && abuild -F -r && cd ~/ &&\
    apk add --allow-untrusted ~/packages/community/x86_64/python2-2.7.18-r4.apk &&\
    wget "https://bootstrap.pypa.io/pip/2.7/get-pip.py" -O get-pip-2.py &&\
    python2 ~/get-pip-2.py &&\
    rm -r ~/aports ~/packages ~/bin-python.patch ~/get-pip-2.py &&\
    apk del .alpine-sdk

CMD ["/bin/bash"]
