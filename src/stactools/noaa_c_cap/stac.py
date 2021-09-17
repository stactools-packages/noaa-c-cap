import logging
from typing import Optional, List

from pystac import Item, MediaType, Collection, Extent
from stactools.core import create

from stactools.noaa_c_cap import Metadata, utils, Dataset
from stactools.noaa_c_cap.constants import COLLECTION_ID, COLLECTION_DESCRIPTION

logger = logging.getLogger(__name__)


def create_collection(hrefs: Optional[List[str]] = None) -> Collection:
    """Creates a STAC Collection for all C-CAP data.

    Args:
        hrefs (Optional[str]): If provided, create a Collection for the provided
        HREFs. If not provided, use the network locations defined in
        `urllist-modres.txt`.
    """
    if not hrefs:
        hrefs = utils.urls()
    datasets = Dataset.from_hrefs(hrefs)
    items = [
        create_item(dataset.tiff_href, dataset.xml_href)
        for dataset in datasets
    ]
    extent = Extent.from_items(items)
    collection = Collection(id=COLLECTION_ID,
                            description=COLLECTION_DESCRIPTION,
                            extent=extent)
    collection.add_items(items)
    return collection


def create_item(tiff_href: str, xml_href: Optional[str] = None) -> Item:
    """Creates a STAC Item for the provided C-CAP tiff file.

    Args:
        tiff_href (str): The HREF pointing to the tiff file.

    Returns:
        Item: STAC Item object
    """
    logger.info(f"Creating STAC item from {tiff_href}")
    item = create.item(tiff_href)
    data = item.assets.get('data')
    assert data
    data.media_type = MediaType.GEOTIFF
    if xml_href:
        metadata = Metadata(xml_href)
        item.datetime = metadata.publication_date
    return item
