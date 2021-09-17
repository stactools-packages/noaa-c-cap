import os.path
from tempfile import TemporaryDirectory
import unittest

import pystac
from stactools.testing import CliTestCase

from stactools.noaa_c_cap.commands import create_noaa_c_cap_command

from tests import test_data


class CommandsTest(CliTestCase):
    def create_subcommand_functions(self):
        return [create_noaa_c_cap_command]

    def test_create_collection(self):
        with TemporaryDirectory() as tmp_dir:
            raise unittest.SkipTest
            destination = os.path.join(tmp_dir, "collection.json")
            result = self.run_command(
                ["noaa-c-cap", "create-collection", destination])
            self.assertEqual(result.exit_code,
                             0,
                             msg="\n{}".format(result.output))
            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)
            collection = pystac.read_file(destination)
            self.assertEqual(collection.id, "my-collection-id")
            collection.validate()

    def test_create_item(self):
        path = test_data.get_external_data(
            'conus_2016_ccap_landcover_20200311.tif')
        with TemporaryDirectory() as tmp_dir:
            destination = os.path.join(tmp_dir, "collection.json")
            result = self.run_command([
                "noaa-c-cap",
                "create-item",
                path,
                destination,
            ])
            self.assertEqual(result.exit_code,
                             0,
                             msg="\n{}".format(result.output))
            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)
            item = pystac.read_file(destination)
            self.assertEqual(item.id, "conus_2016_ccap_landcover_20200311")
            item.validate()
