import datetime
import unittest

from pystac import MediaType

from stactools.noaa_c_cap import stac
from tests import test_data


class StacTest(unittest.TestCase):
    def test_create_collection(self):
        raise unittest.SkipTest
        collection = stac.create_collection()
        self.assertEqual(collection.id, "my-collection-id")
        collection.validate()

    def test_create_item(self):
        path = test_data.get_external_data(
            'conus_2016_ccap_landcover_20200311.tif')
        item = stac.create_item(path)
        self.assertEqual(item.id, 'conus_2016_ccap_landcover_20200311')
        data = item.assets['data']
        self.assertEqual(data.media_type, MediaType.GEOTIFF)
        item.validate()

    def test_create_item_with_xml(self):
        tiff_path = test_data.get_external_data(
            'conus_2016_ccap_landcover_20200311.tif')
        xml_path = test_data.get_path('data-files/CCAP_Parent_2016.xml')
        item = stac.create_item(tiff_path, xml_path)
        self.assertEqual(
            item.datetime,
            datetime.datetime(2016, 10, 3, tzinfo=datetime.timezone.utc))
        item.validate()
