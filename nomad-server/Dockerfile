FROM debian:stable-slim

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

ARG DEBIAN_FRONTEND noninteractive

EXPOSE 4646 4647 4648

VOLUME /etc/nomad/
VOLUME /opt/nomad/

ENV NOMAD_VERSION 1.6.10-1

RUN case "$(uname -m)" in \
    x86_64|amd64) ;; aarch64|arm64|arm64e) ;; \
    *) \
    echo "Unsupported architecture detected, build will fail." \
    exit 1 \
    ;; \
    esac

RUN adduser nomad && usermod -aG nomad nomad &&\
    mkdir -p /opt/nomad && mkdir -p /etc/nomad &&\
    chown -R nomad:nomad /opt/nomad /etc/nomad

RUN apt-get update && apt-get install -y gpg lsb-release wget &&\
    wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg &&\
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list &&\
    apt-get update && apt-get install -y dumb-init nomad=$NOMAD_VERSION &&\
    apt-get remove -y gpg lsb-release wget && apt-get autoremove -y &&\
    apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apt

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
USER nomad
CMD ["nomad", "agent", "-config=/etc/nomad/server.hcl"]
