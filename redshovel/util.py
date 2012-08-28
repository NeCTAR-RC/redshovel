# redshovel provides a simple interface to redmine.
# Copyright (C) 2012 Russell Sim <russell.sim@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import urlparse


def configure_logging(level):
    log_level = logging.WARNING
    if level == 1:
        log_level = logging.INFO
    elif level >= 2:
        log_level = logging.DEBUG

    # Set up basic configuration, out to stderr with a reasonable
    # default format.
    logging.basicConfig(level=log_level)


def get_url(base_url, type):
    if not base_url.endswith("/"):
        base_url = base_url + "/"
    return urlparse.urljoin(base_url, type + ".json")
