import os.path
from tempfile import TemporaryDirectory

import pystac
from stactools.testing import CliTestCase

from stactools.noaa_c_cap.commands import create_noaaccap_command


class CommandsTest(CliTestCase):
    def create_subcommand_functions(self):
        return [create_noaaccap_command]

    def test_create_collection(self):
        with TemporaryDirectory() as tmp_dir:
            # Run your custom create-collection command and validate

            # Example:
            destination = os.path.join(tmp_dir, "collection.json")

            result = self.run_command(
                ["noaaccap", "create-collection", destination])

            self.assertEqual(result.exit_code,
                             0,
                             msg="\n{}".format(result.output))

            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)

            collection = pystac.read_file(destination)
            self.assertEqual(collection.id, "my-collection-id")
            # self.assertEqual(item.other_attr...

            collection.validate()

    def test_create_item(self):
        with TemporaryDirectory() as tmp_dir:
            # Run your custom create-item command and validate

            # Example:
            destination = os.path.join(tmp_dir, "collection.json")
            result = self.run_command([
                "noaaccap",
                "create-item",
                "/path/to/asset.tif",
                destination,
            ])
            self.assertEqual(result.exit_code,
                             0,
                             msg="\n{}".format(result.output))

            jsons = [p for p in os.listdir(tmp_dir) if p.endswith(".json")]
            self.assertEqual(len(jsons), 1)

            item = pystac.read_file(destination)
            self.assertEqual(item.id, "my-item-id")
            # self.assertEqual(item.other_attr...

            item.validate()
