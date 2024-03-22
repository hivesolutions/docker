#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export MAKEFLAGS="-j 16"

export ESP_OPEN_SDK_VERSION="2018-06-10"
export IDF_VERSION="v3.3.6"
export MICROPYTHON_VERSION="v1.22.1"

cd ~

echo "Installing ESP Open SDK..."

# obtains the pre-built version of the ESP Open SDK and unpacks it
# putting it in the expected location
wget https://github.com/jepler/esp-open-sdk/releases/download/$ESP_OPEN_SDK_VERSION/xtensa-lx106-elf-standalone.tar.gz
tar -zxf xtensa-lx106-elf-standalone.tar.gz
rm xtensa-lx106-elf-standalone.tar.gz

# adds the binaries to the path so that they can be used directly
# in the new bash processed from now on (xtensa-lx106 refers to
# the ESP 8266 architecture)
echo "PATH=$(pwd)/xtensa-lx106-elf/bin:\$PATH" >> ~/.profile
source ~/.profile

# clones both the ESP IDF repository and the MicroPython one so that
# they can be latter used for MicroPython related activities
git clone -b $IDF_VERSION --no-recurse-submodules --depth 1 https://github.com/espressif/esp-idf.git
git clone -b $MICROPYTHON_VERSION --no-recurse-submodules --depth=1 https://github.com/micropython/micropython.git

pushd micropython
git submodule update --init lib/axtls lib/berkeley-db-1.xx
make -C mpy-cross
popd
