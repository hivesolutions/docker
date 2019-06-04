#!/bin/bash
# -*- coding: utf-8 -*-

export XTENSA_FILE="xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz"
export IDF_VERSION="v3.1.2"

echo "Installing Espressif ESP32 toolchain..."

cd ~

wget https://dl.espressif.com/dl/$XTENSA_FILE
tar -zxvf $XTENSA_FILE
rm $XTENSA_FILE
echo "PATH=/home/vagrant/xtensa-esp32-elf/bin:\$PATH" >> ~/.profile

git clone --recursive https://github.com/pfalcon/esp-open-sdk.git
pushd esp-open-sdk
make STANDALONE=y
popd

echo "PATH=$(pwd)/xtensa-lx106-elf/bin:\$PATH" >> ~/.profile
source ~/.profile

git clone -b $IDF_VERSION --recursive https://github.com/espressif/esp-idf.git
git clone --recursive https://github.com/micropython/micropython.git
