import logging
import netius.extra

hosts = {
    "hive.pt" : "http://hive-neo-9c45d442.hivesolutions.svc.tutum.io:8001/",
    "cameria.bemisc.com" : "http://cameria-adc13c3f.hivesolutions.svc.tutum.io:8002/",
    "crossline.bemisc.com" : "http://crossline-d3f0b911.hivesolutions.svc.tutum.io:8003/",
    "omnix.bemisc.com" : "http://omnix-0743d1f2.hivesolutions.svc.tutum.io:8004/",
    "lugardajoia.com" : "http://websites-97afa40c.hivesolutions.svc.tutum.io:8005/"
}
server = netius.extra.ReverseProxyServer(
    hosts = hosts
)
server.serve(env = True)
