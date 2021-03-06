# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). This project attempts to match the major and minor versions of [stactools](https://github.com/stac-utils/stactools) and increments the patch number as needed.

## [Unreleased]

## [v0.2.2] - 2022-05-18

### Added

- License link, boundary asset, and more extents ([#17](https://github.com/stactools-packages/noaa-c-cap/pull/17))

## [v0.2.1] - 2022-04-19

### Fixed

- Removed leftover `gsd` attribute -- it is now in `raster:bands` ([#15](https://github.com/stactools-packages/noaa-c-cap/pull/15))

## [v0.2.0] - 2022-04-18

### Added

- `classification` extension ([#12](https://github.com/stactools-packages/noaa-c-cap/pull/12))
- `raster` extension and links ([#13](https://github.com/stactools-packages/noaa-c-cap/pull/13))
- pre-commit ([#13](https://github.com/stactools-packages/noaa-c-cap/pull/13))

### Changed

- All in [#12](https://github.com/stactools-packages/noaa-c-cap/pull/12):
    - Use `pytest` instead of `unittest`
    - Use `black` instead of `yapf`
    - Set datetime to `None`

### Removed

- `file` and `label` extensions ([#12](https://github.com/stactools-packages/noaa-c-cap/pull/12))

## [0.1.4] - 2021-01-19

### Added

- `file` extension

## [0.1.3] - 2022-01-03

### Added

- `read_href_modifier` to `create_item`

## [0.1.2] - 2021-09-22

### Added

- Ability to COGify tiffs while downloading
- Item Assets extension to the Collection
- GSD to Items and Collections
- Constant label classes
- Scientific extension for a citation on the Collection

### Deprecated

- Nothing.

### Removed

- Nothing.

### Fixed

- Nothing.

## [0.1.1] - 2021-09-20

### Added

- Nothing

### Deprecated

- Nothing.

### Removed

- Nothing.

### Fixed

- Lints.

## [0.1.0] - 2021-09-20

Initial commit.

### Added

- Everything.

### Deprecated

- Nothing.

### Removed

- Nothing.

### Fixed

- Nothing.

[Unreleased]: <https://github.com/stactools-packages/noaa-c-cap/compare/v0.2.2..main>
[0.2.2]: <https://github.com/stactools-packages/noaa-c-cap/compare/v0.2.1..v0.2.2>
[0.2.1]: <https://github.com/stactools-packages/noaa-c-cap/compare/v0.2.0..v0.2.1>
[0.2.0]: <https://github.com/stactools-packages/noaa-c-cap/compare/v0.1.4..v0.2.0>
[0.1.4]: <https://github.com/stactools-packages/noaa-c-cap/compare/v0.1.3..v0.1.4>
[0.1.3]: <https://github.com/stactools-packages/noaa-c-cap/compare/v0.1.2..v0.1.3>
[0.1.2]: <https://github.com/stactools-packages/noaa-c-cap/compare/v0.1.1..v0.1.2>
[0.1.1]: <https://github.com/stactools-packages/noaa-c-cap/compare/v0.1.0..v0.1.1>
[0.1.0]: <https://github.com/stactools-packages/noaa-c-cap/releases/tag/v0.1.0>
