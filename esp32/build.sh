#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export MAKEFLAGS="-j 16"

export IDF_VERSION="v4.3.2"
export MICROPYTHON_VERSION="v1.18"

cd ~

echo "Installing Python dependencies..."

pip install --break-system-packages virtualenv

echo "Installing Espressif ESP32 toolchain..."

git clone -b $IDF_VERSION --recursive --depth=1 https://github.com/espressif/esp-idf.git
pushd esp-idf
./install.sh
source export.sh
popd

echo "source $HOME/esp-idf/export.sh" >> ~/.profile

git clone -b $MICROPYTHON_VERSION --no-recurse-submodules --depth=1 https://github.com/micropython/micropython.git

pushd micropython
git submodule update --init lib/axtls lib/berkeley-db-1.xx
make -C mpy-cross
popd
