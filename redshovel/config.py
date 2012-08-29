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

import os
import sys
import optparse
import ConfigParser


class Config(object):
    app_prefix = "RS_"

    def __init__(self, app_name, file="~/.redshovel"):
        """A Config parser that unifies all of the environment,
        config files and arguments.
        """
        usage = "usage: %prog [options]"
        self.optp = optparse.OptionParser(usage=usage)
        self.app_name = app_name
        self.opts = None
        self.args = None

        self.config = ConfigParser.RawConfigParser()
        self.config.read(os.path.expanduser(file))

        # Add the common options.
        self.default_section = set(('api_key', 'url', 'verbose'))
        self.required = set()
        self.add_option("-a", "--api", dest="api_key", required=True,
                        help="The api key to connect to redmine with")
        self.add_option("-u", "--url", dest="url", required=True,
                        help="The url to redmine.")
        self.add_option("-v", "--verbose",
                        action="count", dest="verbose",
                        help="verbosity the more v's the more verbose.")

    def add_option(self, *args, **kwargs):
        if 'required' in kwargs:
            self.required.add(kwargs['dest'])
            del kwargs['required']
        self.optp.add_option(*args, **kwargs)

    def parse_args(self):
        self.opts, self.args = self.optp.parse_args()
        self.validate()
        return self, self.args

    def validate(self):
        """Check that each of the required arguments has been
        specified.  If one of them hasn't then print a message the
        help string and exit.
        """
        for opt in self.required:
            if not getattr(self, opt):
                print "Error: %s is not specified." % opt
                self.optp.print_help()
                sys.exit(1)

    def __getattr__(self, name):
        # Get the operator setting
        ovalue = getattr(self.opts, name, None)
        # Get the environment setting
        evalue = os.environ.get(self.app_prefix + name.upper())

        # Get the config file setting
        section = "DEFAULT" if name in self.default_section else self.app_name
        try:
            cvalue = self.config.get(section, name)
        except ConfigParser.NoOptionError:
            cvalue = None
        except ConfigParser.NoSectionError:
            cvalue = None
        return ovalue or evalue or cvalue
