from stactools.testing.test_data import TestData

EXTERNAL_DATA = {
    "conus_2016_ccap_landcover_20200311.tif": {
        "url": (
            "https://coast.noaa.gov/htdata/raster1/landcover/"
            "bulkdownload/30m_lc/conus_2016_ccap_landcover_20200311.tif"
        ),
        "compress": None,
    },
    "conus_2010_ccap_landcover_20200311.tif": {
        "url": (
            "https://coast.noaa.gov/htdata/raster1/landcover/"
            "bulkdownload/30m_lc/conus_2010_ccap_landcover_20200311.tif"
        ),
        "compress": None,
    },
    "pr_2010_ccap_hr_land_cover20170214_30m.tif": {
        "url": (
            "https://coast.noaa.gov/htdata/raster1/landcover/"
            "bulkdownload/30m_lc/pr_2010_ccap_hr_land_cover20170214_30m.tif"
        ),
        "compress": None,
    },
}

test_data = TestData(__file__, external_data=EXTERNAL_DATA)
