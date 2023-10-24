FROM rust:bookworm AS builder

RUN apt-get update && apt-get install -y -q --no-install-recommends build-essential\
    curl clang cmake libglib2.0-dev lld protobuf-compiler &&\
    cargo install --root /tmp/deno --locked deno

FROM hivesolutions/ubuntu:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /usr/bin/

COPY --from=builder /tmp/deno/bin .

CMD ["/usr/bin/deno --version"]
