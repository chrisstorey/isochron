"""
requests a location from traveltimepy and formats as a tuple
location : str
lat : str
lon : str
"""
import os

import traveltimepy as ttpy

API_ID = os.environ.get('TRAVELTIME_ID', None)
API_KEY = os.environ.get('TRAVELTIME_KEY', None)


def geocode(location: str) -> tuple[str, str]:
    """
    requests a location from traveltimepy and formats as a tuple
    location : str
    lat : str
    lon : str
    """

    result = ttpy.geocoding(location)
    lat = result['features'][0]['geometry']['coordinates'][0]
    lon = result['features'][0]['geometry']['coordinates'][1]
    return lat, lon
