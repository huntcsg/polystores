# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import logging
import sys

logger = logging.getLogger('polystores')


def configure_logger(verbose):
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s',
                        level=log_level,
                        stream=sys.stdout)
