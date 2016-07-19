#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import logging

import netius.extra

hosts = {
    "hive.pt" : "http://ams-logic-1.bemisc.com:8001",
    "hiveinc.co" : "http://ams-logic-1.bemisc.com:8001",
    "www.hive.pt" : "http://ams-logic-1.bemisc.com:8001",
    "www.hiveinc.co" : "http://ams-logic-1.bemisc.com:8001",
    "cameria.bemisc.com" : "http://ams-logic-2.bemisc.com:8002",
    "crossline.bemisc.com" : "http://tutum-crossline.bemisc.com:8003",
    "omnix.bemisc.com" : "http://ams-logic-1.bemisc.com:8004",
    "lugardajoia.com" : "http://ams-logic-2.bemisc.com:8005",
    "www.lugardajoia.com" : "http://ams-logic-2.bemisc.com:8005",
    "passatempo.oibiquini.com" : "http://tutum-websites-oibiquini.bemisc.com:8006",
    "campaigner.bemisc.com" : "http://ams-logic-1.bemisc.com:8007",
    "instashow.bemisc.com" : "http://ams-logic-1.bemisc.com:8008",
    "libs.bemisc.com" : "http://ams-logic-1.bemisc.com:8009",
    "extras.oibiquini.com" : "http://tutum-oibiquini-extras.bemisc.com:8010",
    "repos.bemisc.com" : "http://ams-data-1.bemisc.com:8011",
    "colony.bemisc.com" : "http://ams-data-1.bemisc.com:8011",
    "proyectos.bemisc.com" : "http://tutum-proyectos.bemisc.com:8012",
    "print.bemisc.com" : "http://ams-logic-1.bemisc.com:8013",
    "shopdesk.bemisc.com" : "http://tutum-shopdesk.bemisc.com:8014",
    "hello_quorum.bemisc.com" : "http://tutum-hello-quorum.bemisc.com:8015",
    "hive.frontdoorhd.com" : "http://tutum-omni-hive.bemisc.com:8016",
    "hive.takethebill.com" : "http://tutum-take-the-bill-hive.bemisc.com:8017",
    "metrium.bemisc.com" : "http://ams-logic-2.bemisc.com:8018",
    "webook.pt" : "http://ams-logic-1.bemisc.com:8019",
    "www.webook.pt" : "http://ams-logic-1.bemisc.com:8019",
    "amiranda.frontdoorhd.com" : "http://tutum-omni-amiranda.bemisc.com:8020",
    "amiranda.takethebill.com" : "http://tutum-take-the-bill-amiranda.bemisc.com:8021",
    "blog.hive.pt" : "http://tutum-hive-legacy.bemisc.com:8022/mvc/hive_blog",
    "blog.hivein.co" : "http://tutum-hive-legacy.bemisc.com:8022/mvc/hive_blog",
    "openid.hive.pt" : "http://tutum-hive-legacy.bemisc.com:8022/mvc/hive_openid",
    "openid.hiveinc.co" : "http://tutum-hive-legacy.bemisc.com:8022/mvc/hive_openid",
    "getcolony.com" : "http://tutum-hive-legacy.bemisc.com:8022/mvc/colony_site",
    "www.getcolony.com" : "http://tutum-hive-legacy.bemisc.com:8022/mvc/colony_site",
    "internus.bemisc.com" : "http://ams-logic-1.bemisc.com:8023",
    "joaomagalhaes.eu" : "http://ams-logic-1.bemisc.com:8024",
    "www.joaomagalhaes.eu" : "http://ams-logic-1.bemisc.com:8024",
    "blog.joaomagalhaes.eu" : "http://ams-logic-1.bemisc.com:8024",
    "joamag.com" : "http://ams-logic-1.bemisc.com:8024",
    "www.joamag.com" : "http://ams-logic-1.bemisc.com:8024",
    "joao.me" : "http://ams-logic-1.bemisc.com:8024",
    "www.joao.me" : "http://ams-logic-1.bemisc.com:8024",
    "mailme.bemisc.com" : "http://ams-logic-2.bemisc.com:8025",
    "hello_appier.bemisc.com" : "http://ams-logic-1.bemisc.com:8026",
    "story.bemisc.com" : "http://ams-logic-1.bemisc.com:8027"
}
regex = (
    (re.compile(r"https?://www\.((hive\.pt)|(hiveinc\.co))"), "http://ams-logic-1.bemisc.com:8001"),
    (re.compile(r"https?://blog\.((hive\.pt)|(hiveinc\.co))"), "http://tutum-hive-legacy.bemisc.com:8022/mvc/hive_blog"),
    (re.compile(r"https?://openid\.((hive\.pt)|(hiveinc\.co))"), "http://tutum-hive-legacy.bemisc.com:8022/mvc/hive_openid"),
    (re.compile(r"https?://([a-zA-Z_-]+)\.((hive\.pt)|(hiveinc\.co))/static"), "http://tutum-proyectos.bemisc.com:8012"),
    (re.compile(r"https?://([a-zA-Z_-]+)\.((hive\.pt)|(hiveinc\.co))/appier"), "http://tutum-proyectos.bemisc.com:8012"),
    (re.compile(r"https?://([a-zA-Z_-]+)\.((hive\.pt)|(hiveinc\.co))/render"), "http://tutum-proyectos.bemisc.com:8012"),
    (re.compile(r"https?://([a-zA-Z_-]+)\.((hive\.pt)|(hiveinc\.co))"), "http://tutum-proyectos.bemisc.com:8012/render/{0}"),
)
server = netius.extra.ReverseProxyServer(
    hosts = hosts,
    regex = regex,
    reuse = False
)
server.serve(env = True)
