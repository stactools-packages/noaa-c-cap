from typing import Optional

from pystac import Item, MediaType
from stactools.core import create

from stactools.noaa_c_cap import Metadata


def create_item(tiff_href: str, xml_href: Optional[str] = None) -> Item:
    """Creates a STAC Item for the provided C-CAP tiff file.

    Args:
        tiff_href (str): The HREF pointing to the tiff file.

    Returns:
        Item: STAC Item object
    """
    item = create.item(tiff_href)
    data = item.assets.get('data')
    assert data
    data.media_type = MediaType.GEOTIFF
    if xml_href:
        metadata = Metadata(xml_href)
        item.datetime = metadata.publication_date
    return item
