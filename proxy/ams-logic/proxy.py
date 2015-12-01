import logging
import netius.extra

hosts = {
    "cameria.bemisc.com" : "http://127.0.0.1:8181",
    "omnix.bemisc.com" : "http://127.0.0.1:8282",
    "crossline.bemisc.com" : "http://127.0.0.1:8383"
}
server = netius.extra.ReverseProxyServer(
    hosts = hosts
)
server.serve(env = True)
