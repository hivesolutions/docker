#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export XTENSA_FILE="xtensa-esp32-elf-linux64-1.22.0-97-gc752ad5-5.2.0.tar.gz"
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
make STANDALONE=y

# fixes invalid path of lwip_open library which is meant to be found
# under `usr/lib` by the linker, otherwise linking issues would occur
# when trying to build the Micropython firmware
cp -p xtensa-lx106-elf/xtensa-lx106-elf/sysroot/lib/liblwip_open.a xtensa-lx106-elf/xtensa-lx106-elf/sysroot/usr/lib

popd

# adds the binaries to the path so that they can be used directly
# in the new bash processed from now on (xtensa-lx106 refers to
# the ESP 8266 architecture)
echo "PATH=$(pwd)/xtensa-esp32-elf/bin:\$PATH" >> ~/.profile
echo "PATH=$(pwd)/esp-open-sdk/xtensa-lx106-elf/bin:\$PATH" >> ~/.profile
source ~/.profile

git clone -b $IDF_VERSION --recursive https://github.com/espressif/esp-idf.git
git clone -b $MICROPYTHON_VERSION --recursive https://github.com/micropython/micropython.git

pushd micropython
make -C mpy-cross
pushd ports/esp8266
make
popd
popd
