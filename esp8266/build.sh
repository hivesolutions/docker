#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export XTENSA_FILE="xtensa-esp32-elf-linux64-1.22.0-97-gc752ad5-5.2.0.tar.gz"
export XTENSA_VERSION="1.22.x"
export IDF_VERSION="v3.3.6"
export MICROPYTHON_VERSION="v1.18"

cd ~

echo "Installing Espressif ESP32 toolchain..."

wget https://dl.espressif.com/dl/$XTENSA_FILE
tar -zxvf $XTENSA_FILE
rm $XTENSA_FILE

echo "Installing ESP Open SDK..."

git clone --recursive https://github.com/someburner/esp-open-sdk
pushd esp-open-sdk
pushd crosstool-ng
git checkout xtensa-$XTENSA_VERSION
popd
make STANDALONE=y
popd

# adds the binaries to the path so that they can be used directly
# in the new bash processed from now on
echo "PATH=$(pwd)/xtensa-esp32-elf/bin:\$PATH" >> ~/.profile
echo "PATH=$(pwd)/esp-open-sdk/xtensa-lx106-elf/bin:\$PATH" >> ~/.profile
source ~/.profile

git clone -b $IDF_VERSION --recursive https://github.com/espressif/esp-idf.git
git clone -b $MICROPYTHON_VERSION --recursive https://github.com/micropython/micropython.git

pushd micropython
make -C mpy-cross
popd
