#!/usr/bin/env python
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
import optparse
import urlparse

import requests

LOG = logging.getLogger('rcshibboleth.account-agent')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

usage = "usage: %prog [options]"
optp = optparse.OptionParser(usage=usage)

optp.add_option("-a", "--api", dest="api_key",
                help="The api key to connect to redmine with")
optp.add_option("-u", "--url", dest="url",
                help="The url to redmine.")
optp.add_option("-v", "--verbose",
                action="count", dest="verbose",
                help="verbosity the more v's the more verbose.")


def main():
    optp.add_option('-l', '--limit', dest='limit', action='store', type="int",
                    help="number of results to return.")
    optp.add_option('-o', '--offset', dest='offset', action='store',
                    type="int", help="skip this number of records.")
    optp.add_option('-s', '--sort', dest='sort', action='store',
                    help="sort the results on column.")
    optp.add_option('--status-id', dest='qs_status_id',
                    help="the name of the status state, e.g. closed.")
    optp.add_option('--project-id', dest='qs_project_id',
                    help="the name of the project e.g. rc-support.")
    optp.add_option('--tracker-id', dest='qs_tracker_id',
                    help="the name of the tracker e.g. support.")
    opts, args = optp.parse_args()
    # Here would be a good place to check what came in on the command
    # line and call optp.error("Useful message") to exit if all it not
    # well.

    log_level = logging.WARNING  # default
    if opts.verbose == 1:
        log_level = logging.INFO
    elif opts.verbose >= 2:
        log_level = logging.DEBUG

    # Set up basic configuration, out to stderr with a reasonable
    # default format.
    logging.basicConfig(level=log_level)

    if not opts.url.endswith("/"):
        opts.url = opts.url + "/"
    url = urlparse.urljoin(opts.url, "issues.json")

    headers = {"X-Redmine-API-Key": opts.api_key}
    query = {}
    for qs in dir(opts):
        if qs.startswith("qs_"):
            name = qs[3:]
            query[name] = getattr(opts, qs)

    result = requests.get(url, headers=headers, params=query).json

    from prettytable import PrettyTable
    x = PrettyTable(field_names=["ID", "Tracker", "Status", "Priority",
                    "Title", "Assigned To"])
    for row in result['issues']:
        if 'assigned_to' in row:
            assigned_to = row['assigned_to']['name']
        else:
            assigned_to = ""
        x.add_row([row['id'],
                   row['tracker']['name'],
                   row['status']['name'],
                   row['priority']['name'],
                   row['subject'],
                   assigned_to])
    print str(x)

if __name__ == "__main__":
    main()
