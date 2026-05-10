# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

*

### Changed

*

### Fixed

*

## [1.2.9]

### Changed

* Retry infra-bemisc deployment after upstream fix

## [1.2.8]

### Changed

* Retry infra-bemisc deployment after upstream fix

## [1.2.7]

### Changed

* New CI strategy for infra-bemisc deployment

## [1.2.6]

### Changed

* Bump base netius version

## [1.2.5]

### Changed

* Bump base netius version

## [1.2.4]

### Changed

* Bump base netius version

## [1.2.3]

### Changed

* Log a confirmation line after each SSL context reload / rebuild in `lets-logic`

## [1.2.2]

### Changed

* Delegate SIGHUP reload to netius's bundled `on_config` hook; with the `consul` backend an immediate service refresh is now forced via `_consul_tick(timeout=0)`

## [1.2.1]

### Changed

* Bump netius

## [1.2.0]

### Added

* Forced configuration reload for `lets-logic` on `SIGHUP`, rebuilding ACME rules and SSL contexts via the new netius `config` event

## [1.1.0]

### Added

* Non-root `app` user runs the proxy process for `lets-logic` and `multi-logic`
* SBOM and provenance attestations on the published images

## [1.0.0]

### Changed

* New mono-repo structure with proxy building
* Automation of CI docker file building

### Fixed

* CI automation of docker file building
