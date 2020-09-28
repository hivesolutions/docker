#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export XTENSA_FILE="xtensa-esp32-elf-linux64-1.22.0-96-g2852398-5.2.0.tar.gz"
export IDF_VERSION="v3.3.4"
export MICROPYTHON_VERSION="v1.13"

cd ~

echo "Installing Espressif ESP32 toolchain..."

wget https://dl.espressif.com/dl/$XTENSA_FILE
tar -zxvf $XTENSA_FILE
rm $XTENSA_FILE

echo "Installing ESP Open SDK..."

git clone --recursive https://github.com/pfalcon/esp-open-sdk.git
pushd crosstool-NG
git checkout xtensa-1.22.x
popd
pushd esp-open-sdk
make STANDALONE=y
popd

echo "PATH=$(pwd)/xtensa-esp32-elf/bin:\$PATH" >> ~/.profile
echo "PATH=$(pwd)/esp-open-sdk/xtensa-lx106-elf/bin:\$PATH" >> ~/.profile
source ~/.profile

git clone -b $IDF_VERSION --recursive https://github.com/espressif/esp-idf.git
git clone -b $MICROPYTHON_VERSION --recursive https://github.com/micropython/micropython.git

pushd micropython
make -C mpy-cross
popd
