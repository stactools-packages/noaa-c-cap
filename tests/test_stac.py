import unittest

from stactools.noaa_c_cap import stac

from tests import test_data


class StacTest(unittest.TestCase):
    def test_create_collection(self):
        collection = stac.create_collection()
        self.assertEqual(collection.id, "my-collection-id")
        collection.validate()

    def test_create_item(self):
        path = test_data.get_external_data(
            'conus_2016_ccap_landcover_20200311.tif')
        item = stac.create_item(path)
        self.assertEqual(item.id, 'conus_2016_ccap_landcover_20200311')
        item.validate()
