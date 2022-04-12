from unittest import TestCase

from stactools.noaa_c_cap import Dataset


class DatasetTest(TestCase):
    def test_query_parameters(self) -> None:
        Dataset(
            "https://coast.noaa.gov/htdata/raster1/landcover/bulkdownload/"
            "30m_lc/conus_1975_ccap_landcover_20200311.tif"
            "?a-query-parameter=with_underscores"
        )
