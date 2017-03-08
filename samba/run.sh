#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

adduser admin
smbpasswd -a $PASSWORD

/usr/sbin/smbd -FS
