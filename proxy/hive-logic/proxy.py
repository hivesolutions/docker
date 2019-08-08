#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import logging

import netius.extra
import netius.common

base_port = netius.conf("BASE_PORT", 9001, cast = int)
workers_path = netius.conf("WORKERS_PATH", "/workers")
letse_path = netius.conf("LETSE_PATH", "/data/letsencrypt/etc/live")
auth_passwords = netius.conf("AUTH_PASSWORDS", [], cast = list)
extra_contexts = netius.conf("EXTRA_CONTEXTS", [], cast = list)
host_prefixes = netius.conf(
    "HOST_PREFIXES",
    ["%s.stage.hive.pt", "%s.stage.hive"],
    cast = list
)
forward = netius.conf("FORWARD", None)
host_prefixes += ["%s.proxy"]

hosts = {}
regex = []
auth = {}
auth_regex = []
auth_tuple = []
workers = os.listdir(workers_path)
workers.sort()

for auth_password in auth_passwords:
    simple_auth = netius.SimpleAuth(password = auth_password)
    auth_tuple.append(simple_auth)

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
    hosts["ipv6.hq.hive.pt"] = hosts["viriatum.proxy"]
    hosts["archive.hive.pt"] = hosts["viriatum.proxy"]
    hosts["mirrors.hive.pt"] = hosts["viriatum.proxy"]
    hosts["hq.hive"] = hosts["viriatum.proxy"]
    hosts["archive.hive"] = hosts["viriatum.proxy"]
    hosts["mirrors.hive"] = hosts["viriatum.proxy"]

if "repos.proxy" in hosts:
    hosts["colony.private.hive.pt"] = hosts["repos.proxy"]

if "gitlab.proxy" in hosts:
    for host_prefix in host_prefixes:
        hosts[host_prefix % "gitlab_registry"] = "http://127.0.0.1:5005"
        hosts[host_prefix % "gitlab-registry"] = "http://127.0.0.1:5005"

if "letsencrypt.proxy" in hosts:
    regex.append(
        (
            re.compile(r".+/.well-known/acme-challenge/.+"),
            hosts["letsencrypt.proxy"]
        )
    )
    auth_regex.append(
        (
            re.compile(r".+/.well-known/acme-challenge/.+"),
            None
        )
    )

if "docker.proxy" in hosts and auth_tuple:
    auth["docker.proxy"] = auth_tuple
    auth["docker.stage.hive.pt"] = auth_tuple
    auth["docker.stage.hive"] = auth_tuple

contexts = netius.legacy.keys(hosts) + extra_contexts
server = netius.extra.ReverseProxyServer(
    hosts = hosts,
    regex = regex,
    auth = auth,
    auth_regex = auth_regex,
    forward = forward,
    level = logging.INFO
)
server._ssl_contexts = netius.common.LetsEncryptDict(
    server,
    contexts,
    letse_path = letse_path
)
server.serve(env = True)
