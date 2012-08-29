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

import requests

import util


class RedMineClient(object):
    type = None

    def __init__(self, url, api_key):
        self.headers = {"X-Redmine-API-Key": api_key}
        if not type:
            NotImplementedError("type should be overridden in a sub-class")
        self.url = util.get_url(url, self.type)

    def query(self, query):
        return requests.get(self.url, headers=self.headers, params=query).json
