#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Simple reverse proxy server pointing to a load-balanced back-end
and allowing custom authentication.

Distributes incoming HTTPS traffic across a pool of backend
processes by generating a list of upstream nodes from a base port
and a configurable number of processes. Requests are forwarded
to these nodes in a round-robin fashion via `ReverseProxyServer`.

Authentication is optional and supports two complementary methods
that can be used together:

* Password-based (`SimpleAuth`) - requires a shared secret.
* Address-based (`AddressAuth`) - restricts access by source IP.

Environment / configuration:
    BASE_PORT        - Starting port for the backend pool (default `8080`).
    NUMBER_PROCESSES - Number of backend processes to load-balance (default `8`).
    NODE_TEMPLATE    - URL template for each backend node (default `http://172.17.0.1:%d`).
    AUTH_PASSWORD    - Shared password for `SimpleAuth` (default `None`, disabled).
    AUTH_ADDRESSES   - List of allowed source addresses for `AddressAuth` (default `[]`).
"""

import re

import netius.extra

BASE_PORT = netius.conf("BASE_PORT", 8080, cast=int)
NUMBER_PROCESSES = netius.conf("NUMBER_PROCESSES", 8, cast=int)
NODE_TEMPLATE = netius.conf("NODE_TEMPLATE", "http://172.17.0.1:%d")
AUTH_PASSWORD = netius.conf("AUTH_PASSWORD", None)
AUTH_ADDRESSES = netius.conf("AUTH_ADDRESSES", [], cast=list)

nodes = []

for port in range(BASE_PORT, BASE_PORT + NUMBER_PROCESSES):
    nodes.append(NODE_TEMPLATE % port)

nodes = tuple(nodes)
auth_tuple = []

if AUTH_PASSWORD:
    auth_password = netius.SimpleAuth(password=AUTH_PASSWORD)
else:
    auth_password = None
if AUTH_ADDRESSES:
    auth_address = netius.AddressAuth(AUTH_ADDRESSES)
else:
    auth_address = None

if auth_password:
    auth_tuple.append(auth_password)
if auth_address:
    auth_tuple.append(auth_address)
auth_tuple = tuple(auth_tuple) if auth_tuple else None

regex = ((re.compile(r"https://*"), nodes),)
auth_regex = ((re.compile(r"https://*"), auth_tuple),)
server = netius.extra.ReverseProxyServer(
    regex=regex,
    auth_regex=auth_regex,
)
server.serve(env=True)
