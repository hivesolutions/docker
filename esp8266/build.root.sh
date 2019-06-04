#!/bin/bash
# -*- coding: utf-8 -*-

export TZ=Europe/London
export DEBIAN_FRONTEND=noninteractive

echo "Installing esp-open-sdk, Espressif ESP-IDF, and micropython dependencies..."
echo "Europe/London" > /etc/timezone

apt-get update
apt-get install -y -q build-essential git make unrar-free unzip curl\
    autoconf automake libtool libtool-bin gcc g++ gperf flex bison texinfo gawk ncurses-dev libexpat-dev\
    python python3 sed libreadline-dev libffi-dev pkg-config help2man python-dev python-serial wget sudo
