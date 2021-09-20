import datetime
from typing import List
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

import fsspec


class Metadata:
    publication_date: datetime.datetime
    classes: List[str]

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
        # 2016 CONUS
        allowed_values = xml.findtext(
            'entity-attribute-information/entity/data-attributes/data-attribute/allowed-values'
        )
        # Puerto Rico
        eainfo = xml.find('eainfo')
        # Default
        supplemental_information = xml.findtext(
            'item-identification/supplemental-information')
        if supplemental_information:
            self.classes = parse_supplemental_information(
                supplemental_information)
        elif eainfo:
            self.classes = parse_eainfo(eainfo)
        elif allowed_values:
            self.classes = parse_allowed_values(allowed_values)


def parse_allowed_values(text: str) -> List[str]:
    classes = ['Unclassified']
    for entry in text.split(' | '):
        values = entry.split(': ')
        assert len(values) == 2
        assert int(values[0]) == len(classes)
        classes.append(values[1])
    return classes


def parse_eainfo(eainfo: Element) -> List[str]:
    classes = ['Unclassified']
    for element in eainfo.findall('detailed/attr/attrdomv'):
        text = element.findtext('edom/edomv')
        assert text
        parts = text.split()
        assert (len(parts) >= 2)
        value = int(parts[0])
        assert len(classes) == value
        classes.append(' '.join(parts[1:]))
    return classes


def parse_supplemental_information(text: str) -> List[str]:
    lines = text.splitlines()
    assert (len(lines) > 1)
    classes: List[str] = []
    for line in lines[1:]:
        parts = line.split()
        assert (len(parts) >= 2)
        try:
            value = int(parts[0])
        except ValueError:
            continue
        assert (value == len(classes))
        parts[-1] = parts[-1][0:-1]  # remove trailing comma
        classes.append(' '.join(parts[1:]))
    return classes
