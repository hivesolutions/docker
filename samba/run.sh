#!/bin/bash
# -*- coding: utf-8 -*-

sed -ie "s/{USERNAME}/$USERNAME/g" /etc/samba/smb.conf
sed -ie "s/{WORKGROUP}/$WORKGROUP/g" /etc/samba/smb.conf
sed -ie "s/{ENCRYPTION}/$ENCRYPTION/g" /etc/samba/smb.conf
sed -ie "s/{SIGNING}/$SIGNING/g" /etc/samba/smb.conf

getent passwd $USERNAME > /dev/null 2&>1
if [ ! $? -eq 0 ]; then
    adduser -D $USERNAME
fi

(echo $PASSWORD && echo $PASSWORD) | smbpasswd -a $USERNAME

/usr/sbin/smbd -FS
