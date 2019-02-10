FROM ubuntu:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

ADD build.sh /build.sh
ADD build.root.sh /build.root.sh

RUN /build.root.sh

RUN useradd -ms /bin/bash builder

USER builder

RUN /build.sh
