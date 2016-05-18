#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import logging

import netius.extra
import netius.common

letse_path = netius.conf("LETSE_PATH", "/data/letsencrypt/etc/live")

hosts = {
    "lugardajoia.com" : "http://172.17.0.1:8002",
    "www.lugardajoia.com" : "http://172.17.0.1:8002",
    "budy.lugardajoia.com" : "http://172.17.0.1:8001",
    "ustore.lugardajoia.com" : "http://172.17.0.1:8002"
}
redirect = {
    "lugardajoia.com" : "www.lugardajoia.com"
}
server = netius.extra.ReverseProxyServer(
    hosts = hosts,
    redirect = redirect,
    reuse = False
)
server._ssl_contexts = netius.common.LetsEncryptDict(
    server,
    hosts.keys(),
    letse_path = letse_path
)
server.serve(env = True)
