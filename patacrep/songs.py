#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Song management."""

import re

from patacrep.authors import processauthors
from patacrep.plastex import parsetex

# pylint: disable=too-few-public-methods
class Song(object):
    """Song management"""

    def __init__(self, filename, config):
        # Data extraction from the song with plastex
        data = parsetex(filename)
        self.titles = data['titles']
        self.unprefixed_titles = [
                unprefixed_title(
                    title,
                    config['titleprefixwords']
                    )
                for title
                in self.titles
                ]
        self.args = data['args']
        self.path = filename
        self.languages = data['languages']
        if "by" in self.args.keys():
            self.authors = processauthors(
                    self.args["by"],
                    **config["_compiled_authwords"]
                    )
        else:
            self.authors = []

    def __repr__(self):
        return repr((self.titles, self.args, self.path))

def unprefixed_title(title, prefixes):
    """Remove the first prefix of the list in the beginning of title (if any).
    """
    for prefix in prefixes:
        match = re.compile(ur"^(%s)\b\s*(.*)$" % prefix, re.LOCALE).match(title)
        if match:
            return match.group(2)
    return title

