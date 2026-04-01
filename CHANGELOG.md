# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

* Added module-level documentation to the multi-logic reverse proxy script
* Switched ESP8266 toolchain to MicroPython-hosted standalone esp-open-sdk
* Bumped MicroPython to v1.27.0 for both ESP8266 and ESP32
* Bumped ESP-IDF to v5.5.3 for ESP32
* Pinned Alpine to 3.19 for ESP8266 to avoid GCC 14 C23 incompatibility with Python 2.7
* Replaced defunct jepler/esp-open-sdk with official MicroPython-hosted toolchain
* Removed unnecessary ESP-IDF clone from ESP8266 build (uses NONOS SDK bundled in toolchain)

### Fixed

* Fixed Python 2.7.18 compilation failure caused by GCC 14 C23 reserved keywords
* Fixed broken `get-pip.py` for Python 2.7 by pinning pip < 21 and setuptools < 45
* Fixed missing `-mforce-l32` flag by using correct esp-open-sdk toolchain
* Fixed missing NONOS SDK headers by using standalone toolchain with bundled sysroot
