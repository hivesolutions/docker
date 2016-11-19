#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

import netius.extra
import netius.common

letse_path = netius.conf("LETSE_PATH", "/data/letsencrypt/etc/live")

def on_start(server):
    set_letsencrypt(server)
    set_ssl_contexts(server)

def set_letsencrypt(server):
    if not "letsencrypt" in server.hosts: return
    server.regex.append(
        (
            re.compile(r".+/.well-known/acme-challenge/.+"),
            server.hosts["letsencrypt"]
        )
    )

def set_ssl_contexts(server):
    hosts = netius.legacy.keys(server.hosts)
    alias = netius.legacy.keys(server.alias)
    hosts = list(set(hosts + alias))
    server._ssl_contexts = netius.common.LetsEncryptDict(
        server,
        hosts,
        letse_path = letse_path
    )
    if server.echo: echo_hosts(server, hosts)

def echo_hosts(server, hosts, contexts = None, sort = True):
    contexts = contexts or server._ssl_contexts
    hosts = list(hosts)
    if sort: hosts.sort()
    server.info("Let’s Encrypt host certificate information")
    for host in hosts:
        match = "match" if host in context else "no match"
        server.info("%s => %s" % (host, match))

server = netius.extra.DockerProxyServer()
server.bind("start", on_start)
server.serve(env = True)
