import logging
import os
import pkg_resources

import click
import requests

from stactools.noaa_c_cap import stac

logger = logging.getLogger(__name__)


def create_noaa_c_cap_command(cli):
    """Creates the stactools-noaa-c-cap command line utility."""
    @cli.group(
        "noaa-c-cap",
        short_help=("Commands for working with stactools-noaa-c-cap"),
    )
    def noaa_c_cap():
        pass

    @noaa_c_cap.command(
        "create-collection",
        short_help="Creates a STAC collection",
    )
    @click.argument("destination")
    def create_collection_command(destination: str):
        """Creates a STAC Collection

        Args:
            destination (str): An HREF for the Collection JSON
        """
        collection = stac.create_collection()
        collection.set_self_href(destination)
        collection.save_object()

    @noaa_c_cap.command("create-item", short_help="Create a STAC item")
    @click.argument("source")
    @click.argument("destination")
    def create_item_command(source: str, destination: str):
        """Creates a STAC Item

        Args:
            source (str): HREF of the Asset associated with the Item
            destination (str): An HREF for the STAC Collection
        """
        item = stac.create_item(source)
        item.save_object(dest_href=destination)

    @noaa_c_cap.command(
        "download",
        short_help="Download NOAA C-CAP data into a target directory")
    @click.argument("destination")
    def download_command(destination: str) -> None:
        """Downloads the source data to a target directory.

        Args:
            destinatino (str): A local directory into which the data will downloaded.
        """
        urls = pkg_resources.resource_string(
            __name__, 'urllist-modres.txt').decode('utf-8')
        os.makedirs(destination, exist_ok=True)
        for url in urls.splitlines():
            file_name = os.path.basename(url)
            path = os.path.join(destination, file_name)
            print(f"Downloading {url} to {path}")
            with open(path, 'wb') as f:
                response = requests.get(url, stream=True)
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)

    return noaa_c_cap
