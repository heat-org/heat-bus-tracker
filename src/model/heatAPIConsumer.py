import constant
from location_log import LocationLog
from util import Util


def log_location(lat,lon):
    location = LocationLog(constant.VEHICULOID, lat + ',' + lon)
    return Util.request_post('api/Vehicles/setTrack',location)