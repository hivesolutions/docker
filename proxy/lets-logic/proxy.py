#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Reverse proxy with automatic Let's Encrypt TLS termination and
pluggable service-discovery backends.

Supports two backend engines, selectable via the `BACKEND` configuration
variable:

* `docker` (default) - Uses `DockerProxyServer` to auto-discover
  backend services through the Docker API (via env vars) and route incoming
  HTTP/HTTPS traffic to containers based on their host configuration.
* `consul` - Uses `ConsulProxyServer` to discover services registered
  in Consul's service catalog and route traffic accordingly.

On startup, the proxy:

1. Registers ACME challenge route priority rules so that Let's Encrypt
   HTTP-01 validation requests (`/.well-known/acme-challenge/`) are
   always forwarded to the letsencrypt service - bypassing any
   authentication or HTTPS redirect rules that would otherwise block them.

2. Builds per-host SSL contexts backed by `LetsEncryptDict`, which
   lazily loads certificate/key pairs from the shared Let's Encrypt
   live directory (default `/data/letsencrypt/etc/live`), enabling
   transparent TLS for every configured virtual host.

Environment / configuration:
    BACKEND    - Backend engine: `docker` (default) or `consul`.
    LETSE_PATH - Base path to the Let's Encrypt live certificates directory.
    HOST       - Bind address (default `0.0.0.0`).
    PORT       - Bind port (default `8080`).
    LEVEL      - Logging level (default `INFO`).
    ECHO       - When enabled, logs certificate match status per host at startup.
"""

import re

import netius.extra
import netius.common

ACME_PATTERN = re.compile(r".+/.well-known/acme-challenge/.+")

backend = netius.conf("BACKEND", "docker")
letse_path = netius.conf("LETSE_PATH", "/data/letsencrypt/etc/live")

_letse_url = None
_ssl_hosts = None


def on_start(server):
    set_letsencrypt(server)
    set_ssl_contexts(server)
    server.bind("config", on_config)


def on_stop(server):
    server.unbind("config", on_config)


def on_tick(server):
    set_letsencrypt(server)
    set_ssl_contexts(server)


def on_config(server):
    set_letsencrypt(server, force=True)
    set_ssl_contexts(server, force=True)


def set_letsencrypt(server, force=False):
    global _letse_url

    if not "letsencrypt" in server.hosts:
        return

    letse_url = server.hosts["letsencrypt"]
    if letse_url == _letse_url:
        return
    _letse_url = letse_url

    for rule_list in (server.regex, server.auth_regex, server.redirect_regex):
        rule_list[:] = [entry for entry in rule_list if entry[0] is not ACME_PATTERN]

    server.info("Registering Let's Encrypt ACME rules for %s" % letse_url)

    server.regex.insert(
        0,
        (ACME_PATTERN, letse_url),
    )
    server.auth_regex.insert(0, (ACME_PATTERN, None))
    server.redirect_regex.insert(0, (ACME_PATTERN, None))


def set_ssl_contexts(server, force=False):
    global _ssl_hosts

    hosts = netius.legacy.keys(server.hosts)
    alias = netius.legacy.keys(server.alias)
    redirect = netius.legacy.keys(server.redirect)
    ssl_hosts = frozenset(hosts + alias + redirect)

    if not force and ssl_hosts == _ssl_hosts:
        server.info("Reloading SSL contexts for %d host(s)" % len(ssl_hosts))
        server._ssl_reload()
        return

    _ssl_hosts = ssl_hosts

    server.info("Rebuilding SSL contexts for %d host(s)" % len(ssl_hosts))

    server._ssl_contexts = netius.common.LetsEncryptDict(
        server, list(ssl_hosts), letse_path=letse_path
    )
    if server.echo:
        echo_contexts(server, list(ssl_hosts))


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
server.bind("stop", on_stop)
server.bind("tick", on_tick)
server.serve(env=True)
