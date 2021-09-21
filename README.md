# stactools-noaa-c-cap

- Name: noaa-c-cap
- Package: `stactools.noaa_c_cap`
- PyPI: https://pypi.org/project/stactools-noaa-c-cap/
- Owner: @gadomski
- Dataset homepage: http://github.com/stactools-packages/noaa-c-cap
- STAC extensions used:
  - [proj](https://github.com/stac-extensions/projection/)
  - [label](https://github.com/stac-extensions/label/)
- Extra fields: None

Create STAC Items and Collections for NOAA C-CAP data.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/stactools-packages/noaa-c-cap/main?filepath=docs/installation_and_basic_usage.ipynb)

## Examples

### STAC objects

- [Collection](examples/collection.json)
- [Item](examples/conus_2016_ccap_landcover_20200311/conus_2016_ccap_landcover_20200311.json)

### Command-line usage

Create a single item

```bash
$ stac noaa-c-cap create-item conus_2016_ccap_landcover_20200311.tif item.json
```

Create the entire collection from the remote data sources:

```bash
$ stac noaa-c-ccap create-collection destination-directory
```

Creating the `examples/` directory

```bash
$ stac noaa-c-cap create-collection --catalog-type SELF_CONTAINED examples
```
