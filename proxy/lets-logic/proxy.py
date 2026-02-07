#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Reverse proxy with automatic Let's Encrypt TLS termination and
pluggable service-discovery backends.

Supports two backend engines, selectable via the `BACKEND` configuration
variable:

* `docker` (default) — Uses `DockerProxyServer` to auto-discover
  backend services through the Docker API (via env vars) and route incoming
  HTTP/HTTPS traffic to containers based on their host configuration.
* `consul` — Uses `ConsulProxyServer` to discover services registered
  in Consul's service catalog and route traffic accordingly.

On startup, the proxy:

1. Registers ACME challenge route priority rules so that Let's Encrypt
   HTTP-01 validation requests (`/.well-known/acme-challenge/`) are
   always forwarded to the letsencrypt service — bypassing any
   authentication or HTTPS redirect rules that would otherwise block them.

2. Builds per-host SSL contexts backed by `LetsEncryptDict`, which
   lazily loads certificate/key pairs from the shared Let's Encrypt
   live directory (default `/data/letsencrypt/etc/live`), enabling
   transparent TLS for every configured virtual host.

Environment / configuration:
    BACKEND    — Backend engine: `docker` (default) or `consul`.
    LETSE_PATH — Base path to the Let's Encrypt live certificates directory.
    HOST       — Bind address (default `0.0.0.0`).
    PORT       — Bind port (default `8080`).
    LEVEL      — Logging level (default `INFO`).
    ECHO       — When enabled, logs certificate match status per host at startup.
"""

import re

import netius.extra
import netius.common

backend = netius.conf("BACKEND", "docker")
letse_path = netius.conf("LETSE_PATH", "/data/letsencrypt/etc/live")


def on_start(server):
    set_letsencrypt(server)
    set_ssl_contexts(server)


def set_letsencrypt(server):
    if not "letsencrypt" in server.hosts:
        return
    server.regex.insert(
        0,
        (re.compile(r".+/.well-known/acme-challenge/.+"), server.hosts["letsencrypt"]),
    )
    server.auth_regex.insert(0, (re.compile(r".+/.well-known/acme-challenge/.+"), None))
    server.redirect_regex.insert(
        0, (re.compile(r".+/.well-known/acme-challenge/.+"), None)
    )


def set_ssl_contexts(server):
    hosts = netius.legacy.keys(server.hosts)
    alias = netius.legacy.keys(server.alias)
    redirect = netius.legacy.keys(server.redirect)
    hosts = list(set(hosts + alias + redirect))
    server._ssl_contexts = netius.common.LetsEncryptDict(
        server, hosts, letse_path=letse_path
    )
    if server.echo:
        echo_contexts(server, hosts)


def echo_contexts(server, hosts, contexts=None, sort=True):
    contexts = contexts or server._ssl_contexts
    hosts = list(hosts)
    if sort:
        hosts.sort()
    server.info("Let's Encrypt host context information")
    for host in hosts:
        match = "match" if host in contexts else "no match"
        server.info("%s => %s" % (host, match))


server_classes = dict(
    docker=netius.extra.DockerProxyServer,
    consul=netius.extra.ConsulProxyServer,
)
server_cls = server_classes[backend]
server = server_cls()
server.bind("start", on_start)
server.serve(env=True)
