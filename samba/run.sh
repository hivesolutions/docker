#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

sed -ie "s/{ENCRYPTION}/$ENCRYPTION/g" /etc/samba/smb.conf

adduser -D samba

(echo $PASSWORD && echo $PASSWORD) | smbpasswd -a samba

/usr/sbin/smbd -FS
