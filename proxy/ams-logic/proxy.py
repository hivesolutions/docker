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
    "www.lugardajoia.com" : "http://websites-97afa40c-1.hivesolutions.cont.tutum.io:8005",
    "passatempo.oibiquini.com" : "http://websites-353a812f-1.hivesolutions.cont.tutum.io:8006",
    "campaigner.bemisc.com" : "http://campaigner-4a9f12ed-1.hivesolutions.cont.tutum.io:8007",
    "instashow.bemisc.com" : "http://instashow-17632612-1.hivesolutions.cont.tutum.io:8008",
    "libs.bemisc.com" : "http://libs-2ca151e2-1.hivesolutions.cont.tutum.io:8009",
    "extras.oibiquini.com" : "http://oibiquini-extras-a9d0f203-1.hivesolutions.cont.tutum.io:8010",
    "repos.bemisc.com" : "http://repos-a2dd9087-1.hivesolutions.cont.tutum.io:8011",
    "colony.bemisc.com" : "http://repos-a2dd9087-1.hivesolutions.cont.tutum.io:8011",
    "proyectos.bemisc.com" : "http://proyectos-e2b381d1-1.hivesolutions.cont.tutum.io:8012",
    "print.bemisc.com" : "http://colony-print-fd22a30b-1.hivesolutions.cont.tutum.io:8013",
    "shopdesk.bemisc.com" : "http://shopdesk-4c45ec56-1.hivesolutions.cont.tutum.io:8014",
    "hello_quorum.bemisc.com" : "http://hello-quorum-c444e039-1.hivesolutions.cont.tutum.io:8015",
    "hive.frontdoorhd.com" : "http://omni-3ab9fff2-1.hivesolutions.cont.tutum.io:8016",
    "hive.takethebill.com" : "http://take-the-bill-2bea3565-1.hivesolutions.cont.tutum.io:8017",
    "metrium.bemisc.com" : "http://metrium-930da490-1.hivesolutions.cont.tutum.io:8018",
    "webook.pt" : "http://webook-c8e2419e-1.hivesolutions.cont.tutum.io:8019",
    "www.webook.pt" : "http://webook-c8e2419e-1.hivesolutions.cont.tutum.io:8019",
    "amiranda.frontdoorhd.com" : "http://omni-5061ef71-1.hivesolutions.cont.tutum.io:8020",
    "amiranda.takethebill.com" : "http://take-the-bill-84398ba4-1.hivesolutions.cont.tutum.io:8021",
    "blog.hive.pt" : "http://hive-legacy-eab98775-1.hivesolutions.cont.tutum.io:8022/mvc/hive_blog",
    "openid.hive.pt" : "http://hive-legacy-eab98775-1.hivesolutions.cont.tutum.io:8022/mvc/hive_openid",
    "getcolony.com" : "http://hive-legacy-eab98775-1.hivesolutions.cont.tutum.io:8022/mvc/colony_site",
    "www.getcolony.com" : "http://hive-legacy-eab98775-1.hivesolutions.cont.tutum.io:8022/mvc/colony_site"
}
regex = (
    (re.compile("https?://www\.hive\.pt"), "http://hive-neo-9c45d442-1.hivesolutions.cont.tutum.io:8001"),
    (re.compile("https?://blog\.hive\.pt"), "http://hive-legacy-eab98775-1.hivesolutions.cont.tutum.io:8022/mvc/hive_blog"),
    (re.compile("https?://openid\.hive\.pt"), "http://hive-legacy-eab98775-1.hivesolutions.cont.tutum.io:8022/mvc/hive_openid"),
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
