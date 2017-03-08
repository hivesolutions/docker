#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

adduser -D samba

(echo $PASSWORD && echo $PASSWORD) | smbpasswd -a samba

/usr/sbin/smbd -FS
