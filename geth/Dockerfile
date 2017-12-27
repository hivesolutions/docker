FROM hivesolutions/ubuntu:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

EXPOSE 8545

VOLUME /data

ENV VERSION 1.7.3-4bb3c89d
ENV PLATFORM amd64
ENV HOST 0.0.0.0

RUN wget https://gethstore.blob.core.windows.net/builds/geth-linux-$PLATFORM-$VERSION.tar.gz &&\
    tar -zxvf geth-linux-$PLATFORM-$VERSION.tar.gz && mv geth-linux-$PLATFORM-$VERSION/geth /usr/bin &&\
    rm -rf geth-linux-$PLATFORM-$VERSION

CMD ["/usr/bin/geth", "-rpc", "--rpcaddr", "$HOST", "--datadir", "/data"]
 