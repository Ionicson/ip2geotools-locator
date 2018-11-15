# -*- coding: utf-8 -*-

"""Top-level package for ip2geotools-locator."""

__author__ = """Oldřich Klíma"""
__email__ = 'xklima27@vutbr.cz'
__version__ = '1.0.0'
name = "ip2geotools-locator"

import logging

from ip2geotools_locator.main import Locator

logger = logging.getLogger()
logger.info("###############################################")
logger.info("########## Ip2Geotools-Locator v 1.0 ##########")
logger.info("###############################################")