#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File-system-driven reverse proxy with automatic Let's Encrypt TLS and
per-worker virtual host routing.

Unlike the Docker-aware `lets-logic` proxy, this variant discovers
backend services by scanning a local `workers` directory. Each file in
that directory represents a worker process; the proxy derives a hostname
from the filename and maps it to a sequential localhost port starting at
`BASE_PORT` (default 9001). For every worker, virtual host entries are
generated for each pattern in `HOST_PREFIXES` (e.g.
`<name>.stage.hive.pt`, `<name>.proxy`), with underscores also
normalized to hyphens.

After the worker scan, the proxy applies additional static host aliases
for well-known services (`hq.hive.pt`, `archive.hive.pt`, etc.) and
special-cases like the GitLab container registry (port 5005).

Security and routing layers:

* **ACME challenges** - If a `letsencrypt` worker exists, HTTP-01
  validation requests are routed to it and exempted from authentication.
* **Basic auth** - The `docker` worker endpoint is optionally protected
  via `AUTH_PASSWORDS`.
* **TLS termination** - SSL contexts are loaded per-host from the shared
  Let's Encrypt live directory via `LetsEncryptDict`.

Environment / configuration:
    BASE_PORT      - First port in the sequential worker port range (default 9001).
    WORKERS_PATH   - Directory containing worker descriptor files (default `/workers`).
    LETSE_PATH     - Let's Encrypt live certificates directory (default
                     `/data/letsencrypt/etc/live`).
    AUTH_PASSWORDS - Comma-separated list of passwords for protected endpoints.
    EXTRA_CONTEXTS - Additional hostnames to include in the SSL context map.
    HOST_PREFIXES  - Printf-style patterns for generating virtual hostnames
                     (default `%s.stage.hive.pt`, `%s.stage.hive`).
    FORWARD        - Optional fixed forwarding target override.
"""

import os
import re
import logging

import netius.extra
import netius.common

base_port = netius.conf("BASE_PORT", 9001, cast=int)
workers_path = netius.conf("WORKERS_PATH", "/workers")
letse_path = netius.conf("LETSE_PATH", "/data/letsencrypt/etc/live")
auth_passwords = netius.conf("AUTH_PASSWORDS", [], cast=list)
extra_contexts = netius.conf("EXTRA_CONTEXTS", [], cast=list)
host_prefixes = netius.conf(
    "HOST_PREFIXES", ["%s.stage.hive.pt", "%s.stage.hive"], cast=list
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
    simple_auth = netius.SimpleAuth(password=auth_password)
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
        (re.compile(r".+/.well-known/acme-challenge/.+"), hosts["letsencrypt.proxy"])
    )
    auth_regex.append((re.compile(r".+/.well-known/acme-challenge/.+"), None))

if "docker.proxy" in hosts and auth_tuple:
    auth["docker.proxy"] = auth_tuple
    auth["docker.stage.hive.pt"] = auth_tuple
    auth["docker.stage.hive"] = auth_tuple

contexts = netius.legacy.keys(hosts) + extra_contexts
server = netius.extra.ReverseProxyServer(
    hosts=hosts,
    regex=regex,
    auth=auth,
    auth_regex=auth_regex,
    forward=forward,
    level=logging.INFO,
)
server._ssl_contexts = netius.common.LetsEncryptDict(
    server, contexts, letse_path=letse_path
)
server.serve(env=True)
