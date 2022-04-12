from pystac.provider import Provider, ProviderRole

COLLECTION_ID = "noaa-c-cap"
COLLECTION_TITLE = "C-CAP Regional Land Cover and Change"
COLLECTION_KEYWORDS = ["landcover", "coastal", "change"]
COLLECTION_PROVIDERS = [
    Provider(
        name=(
            "National Oceanic and Atmospheric Administration, "
            "Office for Coastal Management"
        ),
        roles=[
            ProviderRole.LICENSOR,
            ProviderRole.PRODUCER,
            ProviderRole.PROCESSOR,
            ProviderRole.HOST,
        ],
        url="https://coast.noaa.gov/digitalcoast/data/ccapregional.html",
    )
]
COLLECTION_DESCRIPTION = """Nationally standardized, raster-based inventories of \
land cover for the coastal areas of the U.S.  Data are derived, through the \
Coastal Change Analysis Program, from the analysis of multiple dates of remotely \
sensed imagery.  Two file types are available: individual dates that supply a \
wall-to-wall map, and change files that compare one date to another.

The use of standardized data and procedures assures consistency through time and \
across geographies.  C-CAP data forms the coastal expression of the National \
Land Cover Database (NLCD) and the A-16 land cover theme of the National Spatial \
Data Infrastructure.  The data are updated every 5 years."""
CLASSIFICATION_EXTENSION_HREF = (
    "https://stac-extensions.github.io/classification/v1.0.0/schema.json"
)
CLASSIFICATION_CLASSES = [
    {
        "value": 0,
        "description": "Background",
    },
    {
        "value": 1,
        "description": "Unclassified (Cloud, Shadow, etc)",
    },
    {
        "value": 2,
        "description": "High Intensity Developed",
        "color-hint": "FFFFFF",
    },
    {
        "value": 3,
        "description": "Medium Intensity Developed",
        "color-hint": "C1C1C1",
    },
    {
        "value": 4,
        "description": "Low Intensity Developed",
        "color-hint": "979797",
    },
    {
        "value": 5,
        "description": "Developed Open Space",
        "color-hint": "CCCA42",
    },
    {
        "value": 6,
        "description": "Cultivated Crops",
        "color-hint": "4E2409",
    },
    {
        "value": 7,
        "description": "Pasture/Hay",
        "color-hint": "BCA05B",
    },
    {
        "value": 8,
        "description": "Grassland/Herbaceous",
        "color-hint": "EABB8E",
    },
    {
        "value": 9,
        "description": "Deciduous Forest",
        "color-hint": "6FEC48",
    },
    {
        "value": 10,
        "description": "Evergreen Forest",
        "color-hint": "15380A",
    },
    {
        "value": 11,
        "description": "Mixed Forest",
        "color-hint": "489D48",
    },
    {
        "value": 12,
        "description": "Scrub/Shrub",
        "color-hint": "6D6C1F",
    },
    {
        "value": 13,
        "description": "Palustrine Forested Wetland",
        "color-hint": "245A5A",
    },
    {
        "value": 14,
        "description": "Palustrine Scrub/Shrub Wetland",
        "color-hint": "E2742D",
    },
    {
        "value": 15,
        "description": "Palustrine Emergent Wetland (Persistent)",
        "color-hint": "DE3BEA",
    },
    {
        "value": 16,
        "description": "Estuarine Forested Wetland",
        "color-hint": "37083B",
    },
    {
        "value": 17,
        "description": "Estuarine Scrub/Shrub Wetland",
        "color-hint": "631569",
    },
    {
        "value": 18,
        "description": "Estuarine Emergent Wetland",
        "color-hint": "A028A9",
    },
    {
        "value": 19,
        "description": "Unconsolidated Shore",
        "color-hint": "6DEEF0",
    },
    {
        "value": 20,
        "description": "Bare Land",
        "color-hint": "F3F050",
    },
    {
        "value": 21,
        "description": "Open Water",
        "color-hint": "000A72",
    },
    {
        "value": 22,
        "description": "Palustrine Aquatic Bed",
        "color-hint": "0021E8",
    },
    {
        "value": 23,
        "description": "Estuarine Aquatic Bed",
        "color-hint": "6777D4",
    },
    {
        "value": 24,
        "description": "Tundra",
        "color-hint": "F3D147",
    },
    {
        "value": 25,
        "description": "Perennial Ice/Snow",
        "color-hint": "BBF7EF",
    },
]
COLLECTION_CITATION = (
    "National Oceanic and Atmospheric Administration, "
    "Office for Coastal Management. "
    "Name of Data Set: Coastal Change Analysis Program (C-CAP) Regional Land Cover. "
    "Charleston, SC: NOAA Office for Coastal Management. "
    "Accessed Month Year at www.coast.noaa.gov/htdata/raster1/landcover/bulkdownload/30m_lc/."
)
