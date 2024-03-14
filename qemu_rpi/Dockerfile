FROM debian:bookworm-slim

ARG USERNAME=pi
ARG PASSWORD=raspberry

ARG RPI_IMAGE_URL=https://downloads.raspberrypi.org/raspios_arm64/images/raspios_arm64-2023-05-03/2023-05-03-raspios-bullseye-arm64.img.xz
ARG RPI_IMAGE_SHA256=e7c0c89db32d457298fbe93195e9d11e3e6b4eb9e0683a7beb1598ea39a0a7aa
ARG RPI_IMAGE_FILE=2023-05-03-raspios-bullseye-arm64.img

ENV QEMU_MACHINE raspi3b
ENV QEMU_DTB bcm2710-rpi-3-b-plus.dtb
ENV QEMU_CPU cortex-a72
ENV QEMU_MEM 1G
ENV QEMU_CORES 4

EXPOSE 2222

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /qemu

RUN apt-get update -y &&\
    apt-get install -y fdisk mtools openssl python3-minimal qemu-system-aarch64 wget xz-utils

# Downloading RPi image and validating its checksum
RUN wget "${RPI_IMAGE_URL}" -O "${RPI_IMAGE_FILE}.xz" &&\
    echo "${RPI_IMAGE_SHA256} ${RPI_IMAGE_FILE}.xz" | sha256sum -c - &&\
    xz -d ${RPI_IMAGE_FILE}.xz

# Resizing the image to the next power of two as required by QEMU
RUN RPI_IMAGE_SIZE=$(stat -c%s "${RPI_IMAGE_FILE}") &&\
    NEXT_POWER_OF_TWO=$(python3 -c "import math; print(2 ** math.ceil(math.log(int(${RPI_IMAGE_SIZE}), 2)))") &&\
    qemu-img resize "${RPI_IMAGE_FILE}" "${NEXT_POWER_OF_TWO}"

# Extracting kernel and device tree files
RUN SECTOR_SIZE=$(fdisk -lu ${RPI_IMAGE_FILE} | awk '/Sector size/ {print $4}') &&\
    SECTOR_START=$(fdisk -lu ${RPI_IMAGE_FILE} | awk '/W95 FAT32/ {print $2}') &&\
    OFFSET=$((${SECTOR_SIZE}*${SECTOR_START})) &&\
    echo "drive x: file=\"${RPI_IMAGE_FILE}\" offset=${OFFSET}" > ~/.mtoolsrc &&\
    mcopy x:/${QEMU_DTB} . && mcopy x:/kernel8.img .

# Creating user and activating ssh
RUN mkdir -p /tmp && touch /tmp/ssh &&\
    PASSWORD=`openssl passwd -6 ${PASSWORD}` &&\
    echo "${USERNAME}:${PASSWORD}" | tee /tmp/userconf &&\
    mcopy /tmp/ssh x:/ && mcopy /tmp/userconf x:/

# Cleaning up
RUN apt-get autoremove -y && apt-get clean &&\
    rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apt

ENTRYPOINT qemu-system-aarch64 \
    -machine ${QEMU_MACHINE} \
    -dtb ${QEMU_DTB} \
    -cpu ${QEMU_CPU} \
    -smp ${QEMU_CORES} \
    -m ${QEMU_MEM} \
    -sd ${RPI_IMAGE_FILE} \
    -kernel kernel8.img \
    -nographic \
    -append "rw earlyprintk loglevel=8 console=ttyAMA0,115200 dwc_otg.lpm_enable=0 root=/dev/mmcblk0p2 rootdelay=1" \
    -device usb-net,netdev=ulan,mac=b8:27:eb:4f:15:95 \
    -netdev user,id=ulan,hostfwd=tcp::2222-:22
