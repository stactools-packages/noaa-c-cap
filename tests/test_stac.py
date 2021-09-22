import datetime
import os.path
import unittest
from tempfile import TemporaryDirectory

from pystac import MediaType
from pystac.extensions.item_assets import ItemAssetsExtension

from stactools.noaa_c_cap import stac
from stactools.noaa_c_cap.constants import LABEL_CLASSES
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
        self.assertEqual(collection.title,
                         "C-CAP Regional Land Cover and Change")
        self.assertEqual(collection.summaries.get_list("gsd"), [30])
        self.assertEqual(collection.summaries.get_list("label:classes"),
                         [{
                             "classes": LABEL_CLASSES
                         }])
        self.assertEqual(len(list(collection.get_all_items())), 1)

        item_assets = ItemAssetsExtension.ext(collection)
        assert 'data' in item_assets.item_assets
        assert 'metadata' in item_assets.item_assets

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
        self.assertEqual(item.common_metadata.gsd, 30)
        data = item.assets['data']
        self.assertEqual(data.media_type, MediaType.GEOTIFF)
        self.assertEqual(data.roles, ['data'])
        item.validate()

    def test_create_item_with_xml(self):
        tiff_path = test_data.get_external_data(
            'conus_2016_ccap_landcover_20200311.tif')
        xml_path = test_data.get_path('data-files/CCAP_Parent_2016.xml')
        item = stac.create_item(tiff_path, xml_path)
        metadata = item.assets['metadata']
        self.assertEqual(metadata.media_type, MediaType.XML)
        self.assertEqual(metadata.roles, ['metadata'])
        item.validate()

    def test_create_item_2010(self):
        tiff_path = test_data.get_external_data(
            'conus_2016_ccap_landcover_20200311.tif')
        xml_path = test_data.get_path('data-files/CCAP_Parent_2010.xml')
        item = stac.create_item(tiff_path, xml_path)
        item.validate()

    def test_create_item_puerto_rico(self):
        tiff_path = test_data.get_external_data(
            'pr_2010_ccap_hr_land_cover20170214_30m.tif')
        xml_path = test_data.get_path('data-files/2010_puerto_rico_ccap.xml')
        item = stac.create_item(tiff_path, xml_path)
        item.validate()
