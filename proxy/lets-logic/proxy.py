#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

import netius.extra
import netius.common

letse_path = netius.conf("LETSE_PATH", "/data/letsencrypt/etc/live")
extra = netius.conf("EXTRA_CONTEXTS", [], cast = list)

def on_start(server):
    set_letsencrypt(server)
    set_ssl_contexts(server)

def set_letsencrypt(server):
    if not "letsencrypt" in server.hosts: return
    server.regex.insert(0,
        (
            re.compile(r".+/.well-known/acme-challenge/.+"),
            server.hosts["letsencrypt"]
        )
    )
    server.auth_regex.insert(0,
        (
            re.compile(r".+/.well-known/acme-challenge/.+"),
            None
        )
    )

def set_ssl_contexts(server):
    hosts = netius.legacy.keys(server.hosts)
    alias = netius.legacy.keys(server.alias)
    redirect = netius.legacy.keys(server.redirect)
    hosts = list(set(hosts + alias + redirect + extra))
    server._ssl_contexts = netius.common.LetsEncryptDict(
        server,
        hosts,
        letse_path = letse_path
    )
    if server.echo: echo_contexts(server, hosts)

def echo_contexts(server, hosts, contexts = None, sort = True):
    contexts = contexts or server._ssl_contexts
    hosts = list(hosts)
    if sort: hosts.sort()
    server.info("Let’s Encrypt host context information")
    for host in hosts:
        match = "match" if host in contexts else "no match"
        server.info("%s => %s" % (host, match))

server = netius.extra.DockerProxyServer()
server.bind("start", on_start)
server.serve(env = True)
