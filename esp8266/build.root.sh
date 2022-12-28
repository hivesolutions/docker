#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export TZ=Europe/London
export DEBIAN_FRONTEND=noninteractive

echo "Installing esp-open-sdk, Espressif ESP-IDF, and MicroPython dependencies..."
echo "Europe/London" > /etc/timezone

apt-get update
apt-get install -y -q git wget flex bison gperf python2 python3 python3-pip\
    python3-setuptools cmake ninja-build ccache libffi-dev libssl-dev dfu-util libusb-1.0-0

ln -s /usr/bin/python2 /usr/bin/python

wget "https://bootstrap.pypa.io/pip/2.7/get-pip.py"
python get-pip.py
pip install serial
