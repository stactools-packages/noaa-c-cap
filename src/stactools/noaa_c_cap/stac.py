import datetime
import logging
from typing import Optional, List

from pystac import Item, MediaType, Collection, Extent
from pystac.asset import Asset
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
    items = [create_item_from_dataset(dataset) for dataset in datasets]
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
    return create_item_from_dataset(
        Dataset(tiff_href=tiff_href, xml_href=xml_href))


def create_item_from_dataset(dataset: Dataset) -> Item:
    """Creates an item from a NOAA C-CAP dataset."""
    logger.info(f"Creating STAC item from {dataset.tiff_href}")
    item = create.item(dataset.tiff_href)
    item.common_metadata.start_datetime = datetime.datetime(
        int(dataset.year), 1, 1, tzinfo=datetime.timezone.utc)
    item.common_metadata.end_datetime = datetime.datetime(
        int(dataset.year), 12, 31, tzinfo=datetime.timezone.utc)
    item.datetime = item.common_metadata.start_datetime
    data = item.assets.get('data')
    assert data
    data.media_type = MediaType.GEOTIFF
    if dataset.xml_href:
        item.add_asset(
            'metadata',
            Asset(dataset.xml_href,
                  media_type=MediaType.XML,
                  roles=['metadata']))
    return item
