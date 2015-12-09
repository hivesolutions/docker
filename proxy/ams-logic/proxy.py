import logging
import netius.extra

hosts = {
    "hive.pt" : "http://hive-neo-9c45d442.hivesolutions.svc.tutum.io:8001/",
    "cameria.bemisc.com" : "http://cameria-adc13c3f.hivesolutions.svc.tutum.io:8002/"
}
server = netius.extra.ReverseProxyServer(
    hosts = hosts
)
server.serve(env = True)
