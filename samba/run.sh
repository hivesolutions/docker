#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

sed -ie "s/{ENCRYPTION}/$ENCRYPTION/g" /etc/samba/smb.conf
sed -ie "s/{SIGNING}/$SIGNING/g" /etc/samba/smb.conf

getent passwd samba > /dev/null 2&>1

if [ $? -eq 0 ]; then
else
    adduser -D samba
fi

(echo $PASSWORD && echo $PASSWORD) | smbpasswd -a samba

/usr/sbin/smbd -FS
