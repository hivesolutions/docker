import re
import logging
import netius.extra

hosts = {
    "hive.pt" : "http://178.62.246.67:8001",
    "www.hive.pt" : "http://178.62.246.67:8001",
    "cameria.bemisc.com" : "http://cameria-adc13c3f-1.hivesolutions.cont.tutum.io:8002",
    "crossline.bemisc.com" : "http://crossline-d3f0b911-1.hivesolutions.cont.tutum.io:8003",
    "omnix.bemisc.com" : "http://omnix-0743d1f2-1.hivesolutions.cont.tutum.io:8004",
    "lugardajoia.com" : "http://websites-97afa40c-1.hivesolutions.cont.tutum.io:8005",
    "passatempo.oibiquini.com" : "http://websites-353a812f-1.hivesolutions.cont.tutum.io:8006",
    "campaigner.bemisc.com" : "http://campaigner-4a9f12ed-1.hivesolutions.cont.tutum.io:8007",
    "instashow.bemisc.com" : "http://instashow-17632612-1.hivesolutions.cont.tutum.io:8008/"
}
regex = (
    (re.compile("https?://hive\.pt"), "http://178.62.246.67:8001"),
    (re.compile("https?://www.hive\.pt"), "http://178.62.246.67:8001"),
    (re.compile("https?://([a-zA-Z_]+)\.hive\.pt"), "http://127.0.0.1:8181")
)
server = netius.extra.ReverseProxyServer(
    hosts = hosts,
    regex = regex
)
server.serve(env = True)
