from dataclasses import dataclass
import logging
import os.path
from typing import List, Optional

logger = logging.getLogger(__name__)


@dataclass
class Dataset:
    """A NOAA C-CAP dataset.

    Could be CONUS, could be somewhere else. Always has a tiff file, can have XML metadata.
    """
    tiff_href: str
    xml_href: Optional[str]

    @classmethod
    def from_hrefs(cls, hrefs: List[str]) -> List['Dataset']:
        """Creates one or more datasets from a list of hrefs.

        Does the work of looking through the HREFs to associate tifs with xml metadata.
        """
        datasets = []
        for tif_href in (href for href in hrefs
                         if os.path.splitext(href)[1] == '.tif'):
            file_name = os.path.basename(tif_href)
            parts = file_name.split('_')
            if len(parts) < 2:
                raise ValueError(f"Invalid NOAA C-CAP file name: {file_name}")
            location = parts[0]
            year = parts[1]
            if location == 'conus':
                xml_file_name: Optional[str] = f"CCAP_Parent_{year}.xml"
            elif location == 'hi':
                xml_file_name = None
            elif location == 'pr':
                xml_file_name = f"{year}_puerto_rico_ccap.xml"

            if xml_file_name:
                xml_href = next((href for href in hrefs
                                 if os.path.basename(href) == xml_file_name),
                                None)
                if not xml_href:
                    logger.warn(
                        f"Could not find XML metadata file for {tif_href}")
            else:
                xml_href = None

            if not xml_href:
                datasets.append(Dataset(tif_href, None))
            else:
                datasets.append(Dataset(tif_href, xml_href))

        return datasets
