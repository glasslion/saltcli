#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import print_function

import click

from .__init__ import __version__


class SaltCli(object):
    """
    The CLI implementation.
    """

    def run_cli(self):
        """
        Run the main loop
        """
        print(u'Version:', __version__)
        print(u'Home: https://github.com/glasslion/saltcli')


@click.command()
def cli():
    """
    Create and call the CLI
    """
    saltcli = SaltCli()
    saltcli.run_cli()

if __name__ == "__main__":
    cli()
