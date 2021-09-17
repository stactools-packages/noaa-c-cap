import datetime
from xml.etree import ElementTree

import fsspec


class Metadata:
    publication_date: datetime.datetime

    def __init__(self, href: str):
        with fsspec.open(href) as file:
            string = file.read()
        xml = ElementTree.fromstring(string)
        publication_date = xml.findtext('item-identification/publication-date')
        if publication_date:
            self.publication_date = datetime.datetime.strptime(
                publication_date,
                r'%Y-%m-%d').replace(tzinfo=datetime.timezone.utc)
        else:
            timeperd = xml.findtext(
                'idinfo/timeperd/timeinfo/sngdate/caldate')  # puerto rico
            if timeperd:
                self.publication_date = datetime.datetime.strptime(
                    timeperd, r'%Y%m%d')
