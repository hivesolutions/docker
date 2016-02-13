FROM alpine:latest
MAINTAINER Hive Solutions

RUN apk update && apk add bash openssl ca-certificates python python3
RUN wget "https://bootstrap.pypa.io/get-pip.py" && python3 get-pip.py && python get-pip.py && rm get-pip.py

CMD ["/bin/bash"]
