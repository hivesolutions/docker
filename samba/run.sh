#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

adduser -D admin

(echo $PASSWORD && echo $PASSWORD) | smbpasswd -a admin

/usr/sbin/smbd -FS
