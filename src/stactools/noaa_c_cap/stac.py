from typing import Optional

from pystac import Collection, Item, MediaType

from stactools.core import create

from stactools.noaa_c_cap import Metadata


def create_collection() -> Collection:
    """Create a STAC Collection

    This function includes logic to extract all relevant metadata from
    an asset describing the STAC collection and/or metadata coded into an
    accompanying constants.py file.

    See `Collection<https://pystac.readthedocs.io/en/latest/api.html#collection>`_.

    Returns:
        Collection: STAC Collection object
    """
    raise NotImplementedError


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
