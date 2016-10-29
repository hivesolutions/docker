#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import logging

import netius.extra

hosts = {
}
regex = (
    (re.compile(r"*"), "http://libs:8080")
)
server = netius.extra.ReverseProxyServer(
    hosts = hosts,
    regex = regex,
    reuse = False
)
server.serve(env = True)
