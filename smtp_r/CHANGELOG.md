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

## [1.1.0]

### Added

* Non-root `app` user runs the SMTP relay process
* SBOM and provenance attestations on the published image

### Changed

* Internal SMTP port moved from `25` to `2525` so the process can bind without
  root privileges. Consumers must update port mappings (e.g. `-p 25:2525`).

### Fixed

*

## [1.0.0]

### Added

*

### Changed

* New mono-repo structure with smtp-r building
* Automation of CI docker file building

### Fixed

*
