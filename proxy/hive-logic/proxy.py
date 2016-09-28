#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import logging

import netius.extra
import netius.common

base_port = netius.conf("BASE_PORT", 9001, cast = int)
auth_password = netius.conf("AUTH_PASSWORD", None)
workers_path = netius.conf("WORKERS_PATH", "/workers")
letse_path = netius.conf("LETSE_PATH", "/data/letsencrypt/etc/live")
host_prefixes = netius.conf(
    "HOST_PREFIXES",
    ["%s.stage.hive.pt", "%s.stage.hive"],
    cast = list
)
host_prefixes += ["%s.proxy"]

hosts = {}
regex = []
auth = {}
workers = os.listdir(workers_path)
workers.sort()

for worker in workers:
    base, _extension = os.path.splitext(worker)
    base_parts = base.split("-", 1)
    base = base_parts[1] if len(base_parts) > 1 else base_parts[0]
    for host_prefix in host_prefixes:
        host = host_prefix % base
        host_u = host.replace("_", "-")
        hosts[host] = "http://127.0.0.1:%d" % base_port
        hosts[host_u] = "http://127.0.0.1:%d" % base_port
    base_port += 1

if "viriatum.proxy" in hosts:
    hosts["hq.hive.pt"] = hosts["viriatum.proxy"]
    hosts["archive.hive.pt"] = hosts["viriatum.proxy"]
    hosts["mirrors.hive.pt"] = hosts["viriatum.proxy"]
    hosts["hq.hive"] = hosts["viriatum.proxy"]
    hosts["archive.hive"] = hosts["viriatum.proxy"]
    hosts["mirrors.hive"] = hosts["viriatum.proxy"]

if "repos.proxy" in hosts:
    hosts["colony.private.hive.pt"] = hosts["repos.proxy"]

if "letsencrypt.proxy" in hosts:
    regex.append(
        (
            re.compile(r".+/.well-known/acme-challenge/.+"),
            hosts["letsencrypt.proxy"]
        )
    )

if "docker.proxy" in hosts and auth_password:
    auth_tuple = (netius.SimpleAuth(password = auth_password),)
    auth["docker.proxy"] = auth_tuple
    auth["docker.stage.hive.pt"] = auth_tuple
    auth["docker.stage.hive"] = auth_tuple

server = netius.extra.ReverseProxyServer(
    hosts = hosts,
    regex = regex,
    auth = auth,
    level = logging.INFO
)
server._ssl_contexts = netius.common.LetsEncryptDict(
    server,
    hosts.keys(),
    letse_path = letse_path
)
server.serve(env = True)
