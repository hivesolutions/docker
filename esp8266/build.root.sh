#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export TZ=Europe/London
export DEBIAN_FRONTEND=noninteractive

echo "Installing esp-open-sdk, Espressif ESP-IDF, and micropython dependencies..."
echo "Europe/London" > /etc/timezone

apt-get update
apt-get install -y -q build-essential git make unrar-free unzip curl\
    autoconf automake libtool libtool-bin gcc g++ gperf flex bison texinfo gawk ncurses-dev libexpat-dev\
    python2 python3 sed libreadline-dev libffi-dev pkg-config help2man python2-dev python3-dev python3-serial wget sudo

ln -s /usr/bin/python2 /usr/bin/python

wget "https://bootstrap.pypa.io/pip/2.7/get-pip.py"
python get-pip.py
pip install serial
