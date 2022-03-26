#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export IDF_VERSION="v4.3.2"
export MICROPYTHON_VERSION="v1.18"

cd ~

echo "Installing Espressif ESP32 toolchain..."

git clone -b $IDF_VERSION --recursive https://github.com/espressif/esp-idf.git
pushd esp-idf
./install.sh
source export.sh
popd

echo "source $HOME/esp-idf/export.sh" >> ~/.profile

git clone -b $MICROPYTHON_VERSION --recursive https://github.com/micropython/micropython.git

pushd micropython
make -C mpy-cross
popd
