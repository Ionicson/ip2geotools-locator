"""Module for connecting to Eurek DB"""
from ip2geotools.databases.commercial import Eurek
from ip2geotools.errors import (InvalidRequestError, InvalidResponseError,
                                IpAddressNotFoundError, LimitExceededError,
                                LocationError, PermissionRequiredError,
                                ServiceError)
from ip2geotools_locator.folium_map import FoliumMap
from ip2geotools_locator.utils import LOGGER as logger


class EurekDB:
    """
    Class for handling DB connection into Eurek Database
    """
    # instance of map for placing markers
    m = FoliumMap()
    db_data = None

    def __init__(self):
        pass

    def get_location(self, ip_address):
        """
        Retrieves location for given IP address from Eurek database
        Validation and exception handling included.
        """
        try:
            # Try to get and return location
            self.db_data = Eurek.get(ip_address)

            if self.db_data.latitude is None or self.db_data.longitude is None:
                raise InvalidResponseError

            logger.info("DB returned location %.3f N, %.3f E", self.db_data.latitude, self.db_data.longitude)
            return self.db_data

        except (IpAddressNotFoundError, TypeError) as exception:
            # Handling for IpAddressNotFoundError exception
            logger.warning("Database could not find IP address. IpAddressNotFoundError: %s ", str(exception))

        except PermissionRequiredError as exception:
            # Handling for PermissionRequiredError exception
            logger.critical("Additional setings required for DB. PermissionRequiredError: %s ", str(exception))

        except ServiceError as exception:
            # Handling for ServiceError exception
            logger.error("Service is unavailable. ServiceError: %s ", str(exception))

        except LimitExceededError as exception:
            # Handling for LimitExceededError exception
            logger.warning("Database Eurek has exceeded number of requests! LimitExceededError")

        except (LocationError, InvalidRequestError, InvalidResponseError) as exception:
            # Handling for invalid data, request and response exception
            logger.error("Database Eurek returned %s ", str(exception.__class__))

    def add_to_map(self):
        """
        Add Folium Marker to map. Call get_location(ip) method before adding any markers to map!
        """

        logger.debug("Calling add_marker method for %s DB", Eurek.__name__)
        if self.db_data is not None:
            self.m.add_marker(Eurek.__name__, self.db_data, True)
        else:
            logger.warning("Cannot add empty marker db %s", Eurek.__name__)
