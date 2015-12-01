import logging
import netius.extra

hosts = {
    "cameria.bemisc.com" : "http://hive-neo-9c45d442.hivesolutions.svc.tutum.io:8001"
}
server = netius.extra.ReverseProxyServer(
    hosts = hosts
)
server.serve(env = True)
