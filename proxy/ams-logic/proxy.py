#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import logging
import netius.extra

hosts = {
    "hive.pt" : "http://hive-neo-06808309-1.hivesolutions.cont.tutum.io:8001",
    "hiveinc.co" : "http://hive-neo-06808309-1.hivesolutions.cont.tutum.io:8001",
    "www.hive.pt" : "http://hive-neo-06808309-1.hivesolutions.cont.tutum.io:8001",
    "www.hiveinc.co" : "http://hive-neo-06808309-1.hivesolutions.cont.tutum.io:8001",
    "cameria.bemisc.com" : "http://cameria-adc13c3f-1.hivesolutions.cont.tutum.io:8002",
    "crossline.bemisc.com" : "http://crossline-d3f0b911-1.hivesolutions.cont.tutum.io:8003",
    "omnix.bemisc.com" : "http://omnix-0743d1f2-1.hivesolutions.cont.tutum.io:8004",
    "lugardajoia.com" : "http://websites-ldj-3c8e8b34-1.hivesolutions.cont.tutum.io:8005",
    "www.lugardajoia.com" : "http://websites-ldj-3c8e8b34-1.hivesolutions.cont.tutum.io:8005",
    "passatempo.oibiquini.com" : "http://websites-oibiquini-3c11ae3e-1.hivesolutions.cont.tutum.io:8006",
    "campaigner.bemisc.com" : "http://campaigner-4a9f12ed-1.hivesolutions.cont.tutum.io:8007",
    "instashow.bemisc.com" : "http://instashow-17632612-1.hivesolutions.cont.tutum.io:8008",
    "libs.bemisc.com" : "http://libs-2ca151e2-1.hivesolutions.cont.tutum.io:8009",
    "extras.oibiquini.com" : "http://oibiquini-extras-24badc01-1.hivesolutions.cont.tutum.io:8010",
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
    "blog.hive.pt" : "http://hive-legacy-0d6bac2d-1.hivesolutions.cont.tutum.io:8022/mvc/hive_blog",
    "blog.hivein.co" : "http://hive-legacy-0d6bac2d-1.hivesolutions.cont.tutum.io:8022/mvc/hive_blog",
    "openid.hive.pt" : "http://hive-legacy-0d6bac2d-1.hivesolutions.cont.tutum.io:8022/mvc/hive_openid",
    "openid.hiveinc.co" : "http://hive-legacy-0d6bac2d-1.hivesolutions.cont.tutum.io:8022/mvc/hive_openid",
    "getcolony.com" : "http://hive-legacy-0d6bac2d-1.hivesolutions.cont.tutum.io:8022/mvc/colony_site",
    "www.getcolony.com" : "http://hive-legacy-0d6bac2d-1.hivesolutions.cont.tutum.io:8022/mvc/colony_site",
    "internus.bemisc.com" : "http://internus-f596ab5f-1.hivesolutions.cont.tutum.io:8023",
    "joaomagalhaes.eu" : "http://joamag-neo-aa18f272-1.hivesolutions.cont.tutum.io:8024",
    "www.joaomagalhaes.eu" : "http://joamag-neo-aa18f272-1.hivesolutions.cont.tutum.io:8024",
    "blog.joaomagalhaes.eu" : "http://joamag-neo-aa18f272-1.hivesolutions.cont.tutum.io:8024",
    "joamag.com" : "http://joamag-neo-aa18f272-1.hivesolutions.cont.tutum.io:8024",
    "www.joamag.com" : "http://joamag-neo-aa18f272-1.hivesolutions.cont.tutum.io:8024",
    "joao.me" : "http://joamag-neo-aa18f272-1.hivesolutions.cont.tutum.io:8024",
    "www.joao.me" : "http://joamag-neo-aa18f272-1.hivesolutions.cont.tutum.io:8024",
    "mailme.bemisc.com" : "http://mailme-ed9d9cea-1.hivesolutions.cont.tutum.io:8025",
    "hello_appier.bemisc.com" : "http://hello-appier-9bf14b98-1.hivesolutions.cont.tutum.io:8026",
    "story.bemisc.com" : "http://story-2330baee-1.hivesolutions.cont.tutum.io:8027"
}
regex = (
    (re.compile(r"https?://www\.((hive\.pt)|(hiveinc\.co))"), "http://hive-neo-06808309-1.hivesolutions.cont.tutum.io:8001"),
    (re.compile(r"https?://blog\.((hive\.pt)|(hiveinc\.co))"), "http://hive-legacy-0d6bac2d-1.hivesolutions.cont.tutum.io:8022/mvc/hive_blog"),
    (re.compile(r"https?://openid\.((hive\.pt)|(hiveinc\.co))"), "http://hive-legacy-0d6bac2d-1.hivesolutions.cont.tutum.io:8022/mvc/hive_openid"),
    (re.compile(r"https?://([a-zA-Z_]+)\.((hive\.pt)|(hiveinc\.co))/static"), "http://proyectos-e2b381d1-1.hivesolutions.cont.tutum.io:8012"),
    (re.compile(r"https?://([a-zA-Z_]+)\.((hive\.pt)|(hiveinc\.co))/appier"), "http://proyectos-e2b381d1-1.hivesolutions.cont.tutum.io:8012"),
    (re.compile(r"https?://([a-zA-Z_]+)\.((hive\.pt)|(hiveinc\.co))/render"), "http://proyectos-e2b381d1-1.hivesolutions.cont.tutum.io:8012"),
    (re.compile(r"https?://([a-zA-Z_]+)\.((hive\.pt)|(hiveinc\.co))"), "http://proyectos-e2b381d1-1.hivesolutions.cont.tutum.io:8012/render/{0}"),
)
server = netius.extra.ReverseProxyServer(
    hosts = hosts,
    regex = regex,
    reuse = False
)
server.serve(env = True)
