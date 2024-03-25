#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export MAKEFLAGS="-j 16"

export TZ=Europe/London
export DEBIAN_FRONTEND=noninteractive
export PYTHON_VERSION="2.7.18"

echo "Installing esp-open-sdk, Espressif ESP-IDF, and MicroPython dependencies..."
echo "Europe/London" > /etc/timezone

apk update
apk add gcompat git wget curl gcc g++ make flex bison gperf python3 py3-pip cmake\
    ccache libffi-dev openssl-dev zlib-dev

wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
tar -zxf Python-$PYTHON_VERSION.tgz
rm Python-$PYTHON_VERSION.tgz

# jumps into the Python directory, configures the build, compiles it, and
# installs it in the system
pushd Python-$PYTHON_VERSION
./configure --prefix=/usr && make && make install
popd

wget "https://bootstrap.pypa.io/pip/2.7/get-pip.py"
python get-pip.py
pip install "pyyaml<5" serial
