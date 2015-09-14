#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import print_function
import logging

import click
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.shortcuts import get_input

from .__init__ import __version__


class SaltCli(object):
    """
    The CLI implementation.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.id_completer = WordCompleter([
            'id1', 'id2', 'id3'
        ])


    def run_cli(self):
        """
        Run the main loop
        """
        print(u'Version:', __version__)
        print(u'Home: https://github.com/glasslion/saltcli')

        while True:
            text = get_input(u"> ", completer=self.id_completer)

            print(u'You entered:', text)


@click.command()
def cli():
    """
    Create and call the CLI
    """
    saltcli = SaltCli()
    saltcli.run_cli()

if __name__ == "__main__":
    cli()
