#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

import netius.extra
import netius.common

letse_path = netius.conf("LETSE_PATH", "/data/letsencrypt/etc/live")

def set_letsencrypt(server):
    if not "letsencrypt" in server.hosts: return
    server.regex.append(
        (
            re.compile(r".+/.well-known/acme-challenge/.+"),
            server.hosts["letsencrypt"]
        )
    )

def set_ssl_contexts(server):
    server._ssl_contexts = netius.common.LetsEncryptDict(
        server,
        server.hosts.keys(),
        letse_path = letse_path
    )

def on_start(server):
    set_letsencrypt(server)
    set_ssl_contexts(server)

server = netius.extra.DockerProxyServer()
server.bind("start", on_start)
server.serve(env = True)
