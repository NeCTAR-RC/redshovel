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

from config import Config
from client import RedMineClient
import util

LOG = logging.getLogger('redshovel.issue')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class IssueClient(RedMineClient):
    type = 'issues'


def main():
    conf = Config('rs-issue')
    conf.add_option('-l', '--limit', dest='limit', action='store', type="int",
                    help="number of results to return.")
    conf.add_option('-o', '--offset', dest='offset', action='store',
                    type="int", help="skip this number of records.")
    conf.add_option('-s', '--sort', dest='sort', action='store',
                    help="sort the results on column.")
    conf.add_option('--status-id', dest='qs_status_id',
                    help="the name of the status state, e.g. closed.")
    conf.add_option('--project-id', dest='qs_project_id',
                    help="the name of the project e.g. rc-support.")
    conf.add_option('--tracker-id', dest='qs_tracker_id',
                    help="the name of the tracker e.g. support.")
    opts, args = conf.parse_args()
    # Here would be a good place to check what came in on the command
    # line and call optp.error("Useful message") to exit if all it not
    # well.
    util.configure_logging(opts.verbose)

    query = {}
    for qs in dir(opts):
        if qs.startswith("qs_"):
            name = qs[3:]
            query[name] = getattr(opts, qs)

    client = IssueClient(opts.url, opts.api_key)
    result = client.query(query)

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
