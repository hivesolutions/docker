#!/bin/bash
# -*- coding: utf-8 -*-

set -e +h

export MAKEFLAGS="-j 16"

export MICROPYTHON_VERSION="v1.27.0"

cd ~

echo "Installing ESP SDK..."

# obtains the standalone esp-open-sdk toolchain hosted by MicroPython
# (includes -mforce-l32 patched GCC, NONOS SDK headers/libs in sysroot)
wget https://micropython.org/resources/xtensa-lx106-elf-standalone.tar.gz
tar -zxf xtensa-lx106-elf-standalone.tar.gz
rm xtensa-lx106-elf-standalone.tar.gz

# adds the binaries to the path so that they can be used directly
# in the new bash processed from now on (xtensa-lx106 refers to the
# ESP 8266 architecture)
echo "PATH=$(pwd)/xtensa-lx106-elf/bin:\$PATH" >> ~/.profile
source ~/.profile

# clones the MicroPython repository so that it can be later used
# for MicroPython related activities
git clone -b $MICROPYTHON_VERSION --no-recurse-submodules --depth=1 https://github.com/micropython/micropython.git

# jumps into the MicroPython directory, initializes some of the submodules
# and compiles the MicroPython cross-compiler (mpy-cross)
pushd micropython
git submodule update --init lib/axtls lib/berkeley-db-1.xx
make -C mpy-cross
popd
