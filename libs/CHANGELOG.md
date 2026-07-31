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

### Changed

* Leaner official base images: `python:alpine` and `pypy:slim`, with repositories cloned in a throwaway build stage so git is not shipped in the final image
* Removed the `oibiquini` static files, the clone relied on a defunct Bitbucket token and was breaking the build

## [1.0.0]

### Added

* SBOM and provenance attestations on the published images

### Changed

* New mono-repo structure with libs building
* Automation of CI docker file building
