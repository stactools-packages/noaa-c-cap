import datetime
import os.path
from tempfile import TemporaryDirectory
import unittest

from pystac import MediaType

from stactools.noaa_c_cap import stac
from tests import test_data


class StacTest(unittest.TestCase):
    def test_create_collection(self):
        hrefs = [
            test_data.get_external_data(
                'conus_2016_ccap_landcover_20200311.tif'),
            test_data.get_path('data-files/CCAP_Parent_2016.xml'),
        ]
        collection = stac.create_collection(hrefs)
        self.assertEqual(collection.id, 'noaa-c-cap')
        self.assertEqual(len(list(collection.get_all_items())), 1)
        with TemporaryDirectory() as directory:
            collection.normalize_hrefs(
                os.path.join(directory, 'collection.json'))
            collection.validate_all()

    def test_create_item(self):
        path = test_data.get_external_data(
            'conus_2016_ccap_landcover_20200311.tif')
        item = stac.create_item(path)
        self.assertEqual(item.id, 'conus_2016_ccap_landcover_20200311')
        self.assertEqual(
            item.datetime,
            datetime.datetime(2016, 1, 1, tzinfo=datetime.timezone.utc))
        self.assertEqual(
            item.common_metadata.start_datetime,
            datetime.datetime(2016, 1, 1, tzinfo=datetime.timezone.utc))
        self.assertEqual(
            item.common_metadata.end_datetime,
            datetime.datetime(2016, 12, 31, tzinfo=datetime.timezone.utc))
        data = item.assets['data']
        self.assertEqual(data.media_type, MediaType.GEOTIFF)
        item.validate()

    def test_create_item_with_xml(self):
        tiff_path = test_data.get_external_data(
            'conus_2016_ccap_landcover_20200311.tif')
        xml_path = test_data.get_path('data-files/CCAP_Parent_2016.xml')
        item = stac.create_item(tiff_path, xml_path)
        item.validate()
