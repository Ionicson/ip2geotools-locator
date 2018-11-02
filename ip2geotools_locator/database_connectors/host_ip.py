from collections import namedtuple
from ip2geotools.databases.noncommercial import HostIP

from ip2geotools_locator.folium_map import FoliumMap

Location = namedtuple('Location', 'latitude longitude')

class HostIpDB:
    m = FoliumMap()
    __db_data = None
    
    def __init__(self):
        pass        

    def get_location(self, ip):
        self.__db_data = HostIP.get(ip)
        loc = Location(self.__db_data.latitude, self.__db_data.longitude)
        
        return loc

    def add_to_map(self):
        self.m.add_marker_noncommercial(HostIP.__name__, self.__db_data.ip_address, self.__db_data.country, self.__db_data.city, self.__db_data.latitude, self.__db_data.longitude)
