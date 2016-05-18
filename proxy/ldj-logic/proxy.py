#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import logging

import netius.extra
import netius.common

auth_password = netius.conf("AUTH_PASSWORD", None)
auth_addresses = netius.conf("AUTH_ADDRESSES", [], cast = list)
letse_path = netius.conf("LETSE_PATH", "/data/letsencrypt/etc/live")

auth_tuple = []
if auth_password: auth_tuple.append(netius.SimpleAuth(password = auth_password))
if auth_addresses: auth_tuple.append(netius.AddressAuth(auth_addresses))
auth_tuple = tuple(auth_tuple) if auth_tuple else None

hosts = {
    "lugardajoia.com" : "http://172.17.0.1:8002",
    "www.lugardajoia.com" : "http://172.17.0.1:8002",
    "budy.lugardajoia.com" : "http://172.17.0.1:8001",
    "ustore.lugardajoia.com" : "http://172.17.0.1:8002"
}
auth_regex = (
    (re.compile(r"https://(www.)?lugardajoia.com/*"), auth_tuple),
    (re.compile(r"https://*"), None)
)
redirect = {
    "lugardajoia.com" : "www.lugardajoia.com"
}
server = netius.extra.ReverseProxyServer(
    hosts = hosts,
    auth_regex = auth_regex,
    redirect = redirect,
    reuse = False
)
server._ssl_contexts = netius.common.LetsEncryptDict(
    server,
    hosts.keys(),
    letse_path = letse_path
)
server.serve(env = True)
