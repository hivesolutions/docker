import re
import logging
import netius.extra

hosts = {
    "hive.pt" : "http://hive-neo-9c45d442-1.hivesolutions.cont.tutum.io:8001",
    "www.hive.pt" : "http://hive-neo-9c45d442-1.hivesolutions.cont.tutum.io:8001",
    "cameria.bemisc.com" : "http://cameria-adc13c3f-1.hivesolutions.cont.tutum.io:8002",
    "crossline.bemisc.com" : "http://crossline-d3f0b911-1.hivesolutions.cont.tutum.io:8003",
    "omnix.bemisc.com" : "http://omnix-0743d1f2-1.hivesolutions.cont.tutum.io:8004",
    "lugardajoia.com" : "http://websites-97afa40c-1.hivesolutions.cont.tutum.io:8005",
    "passatempo.oibiquini.com" : "http://websites-353a812f-1.hivesolutions.cont.tutum.io:8006",
    "campaigner.bemisc.com" : "http://campaigner-4a9f12ed-1.hivesolutions.cont.tutum.io:8007",
    "instashow.bemisc.com" : "http://instashow-17632612-1.hivesolutions.cont.tutum.io:8008",
    "libs.bemisc.com" : "http://libs-2ca151e2-1.hivesolutions.cont.tutum.io:8009",
    "extras.oibiquini.com" : "http://oibiquini-extras-a9d0f203-1.hivesolutions.cont.tutum.io:8010",
    "repos.bemisc.com" : "http://repos-a2dd9087-1.hivesolutions.cont.tutum.io:8011",
    "colony.bemisc.com" : "http://repos-a2dd9087-1.hivesolutions.cont.tutum.io:8011",
    "proyectos.bemisc.com" : "http://proyectos-e2b381d1-1.hivesolutions.cont.tutum.io:8012"
}
regex = (
    (re.compile("https?://([a-zA-Z_]+)\.hive\.pt/static"), "http://proyectos-e2b381d1-1.hivesolutions.cont.tutum.io:8012"),
    (re.compile("https?://([a-zA-Z_]+)\.hive\.pt/appier"), "http://proyectos-e2b381d1-1.hivesolutions.cont.tutum.io:8012"),
    (re.compile("https?://([a-zA-Z_]+)\.hive\.pt/render"), "http://proyectos-e2b381d1-1.hivesolutions.cont.tutum.io:8012"),
    (re.compile("https?://([a-zA-Z_]+)\.hive\.pt"), "http://proyectos-e2b381d1-1.hivesolutions.cont.tutum.io:8012/render/{0}"),
)
server = netius.extra.ReverseProxyServer(
    hosts = hosts,
    regex = regex,
    reuse = False
)
server.serve(env = True)
