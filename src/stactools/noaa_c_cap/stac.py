import datetime
import logging
from typing import List, Optional

from pystac import Asset, Collection, Extent, Item, MediaType
from pystac.extensions.label import LabelClasses, LabelExtension, LabelType
from stactools.core import create

from stactools.noaa_c_cap import Dataset, Metadata, utils
from stactools.noaa_c_cap.constants import (COLLECTION_DESCRIPTION,
                                            COLLECTION_ID, COLLECTION_KEYWORDS,
                                            COLLECTION_PROVIDERS,
                                            COLLECTION_TITLE)

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
                            title=COLLECTION_TITLE,
                            description=COLLECTION_DESCRIPTION,
                            extent=extent,
                            keywords=COLLECTION_KEYWORDS,
                            providers=COLLECTION_PROVIDERS)
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
        label = LabelExtension.ext(item, add_if_missing=True)
        metadata = Metadata(dataset.xml_href)
        label.label_properties = None
        label.label_description = "Land cover classes"
        label.label_type = LabelType.RASTER
        label.label_classes = [
            LabelClasses.create(name='classes', classes=list(metadata.classes))
        ]
    return item
