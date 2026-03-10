#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export MAKEFLAGS="-j 16"

export ESP_SDK_VERSION="gcc8_4_0-esp-2020r3"
export IDF_VERSION="v3.3.6"
export MICROPYTHON_VERSION="v1.22.1"

cd ~

echo "Installing ESP SDK..."

# obtains the pre-built version of the Xtensa toolchain from the
# official Espressif download server and unpacks it
wget https://dl.espressif.com/dl/xtensa-lx106-elf-${ESP_SDK_VERSION}-linux-amd64.tar.gz
tar -zxf xtensa-lx106-elf-${ESP_SDK_VERSION}-linux-amd64.tar.gz
rm xtensa-lx106-elf-${ESP_SDK_VERSION}-linux-amd64.tar.gz

# adds the binaries to the path so that they can be used directly
# in the new bash processed from now on (xtensa-lx106 refers to
# the ESP 8266 architecture)
echo "PATH=$(pwd)/xtensa-lx106-elf/bin:\$PATH" >> ~/.profile
source ~/.profile

# clones both the ESP IDF repository and the MicroPython one so that
# they can be latter used for MicroPython related activities
git clone -b $IDF_VERSION --no-recurse-submodules --depth 1 https://github.com/espressif/esp-idf.git
git clone -b $MICROPYTHON_VERSION --no-recurse-submodules --depth=1 https://github.com/micropython/micropython.git

# jumps into the MicroPython directory, initializes some of the submodules
# and compiles the MicroPython cross-compiler (mpy-cross)
pushd micropython
git submodule update --init lib/axtls lib/berkeley-db-1.xx
make -C mpy-cross
popd
