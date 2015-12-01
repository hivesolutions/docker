import logging
import netius.extra

hosts = {
    "cameria.bemisc.com" : "http://127.0.0.1:8181",
    "omnix.bemisc.com" : "http://127.0.0.1:8282",
    "crossline.bemisc.com" : "http://127.0.0.1:8383",
    "lugardajoia.com" : "http://127.0.0.1:8484",
    "www.lugardajoia.com" : "http://127.0.0.1:8484",
    "libs.bemisc.com" : "http://127.0.0.1:8585",
    "print.bemisc.com" : "http://127.0.0.1:8686",
    "campaigner.bemisc.com" : "http://127.0.0.1:8787",
    "passatempo.oibiquini.com" : "http://127.0.0.1:8888",
    "shopdesk.bemisc.com" : "http://127.0.0.1:8989",
    "extras.oibiquini.com" : "http://127.0.0.1:9090",
    "colony.bemisc.com" : "http://127.0.0.1:9191",
    "instashow.bemisc.com" : "http://127.0.0.1:9292"
}
server = netius.extra.ReverseProxyServer(
    hosts = hosts
)
server.serve(env = True)
