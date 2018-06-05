FROM ubuntu:latest

LABEL version="1.0"
LABEL maintainer="Hive Solutions <development@hive.pt>"

RUN echo "Installing esp-open-sdk, Espressif ESP-IDF, and micropython dependencies..." &&\
    apt-get update &&\
    apt-get install -y -q build-essential git make unrar-free unzip\
        autoconf automake libtool libtool-bin gcc g++ gperf\
        flex bison texinfo gawk ncurses-dev libexpat-dev\
        python sed libreadline-dev libffi-dev pkg-config\
        help2man python-dev python-serial wget sudo &&\
    echo "Installing Espressif ESP32 toolchain..." &&\
    cd ~ &&\
    wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz 2> /dev/null &&\
    tar xvfz xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz &&\
    echo "PATH=/home/vagrant/xtensa-esp32-elf/bin:\$PATH" >> ~/.profile &&\
    echo "Installing esp-open-sdk, Espressif ESP-IDF, and micropython source..." &&\
    git clone --recursive https://github.com/pfalcon/esp-open-sdk.git &&\
    git clone --recursive https://github.com/espressif/esp-idf.git &&\
    git clone https://github.com/micropython/micropython.git
