#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import print_function
import logging
import os.path

import click
from prompt_toolkit import CommandLineInterface, Application, AbortAction
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.shortcuts import create_prompt_layout, create_eventloop

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

        history = FileHistory(os.path.expanduser('~/.saltcli-history'))

        layout = create_prompt_layout(
            message=u'saltcli> ',
        )

        application = Application(
            layout=layout
        )

        eventloop = create_eventloop()

        self.cli = CommandLineInterface(
            application=application,
            eventloop=eventloop)

        while True:
            try:
                document = self.cli.run()
            except OptionError as ex:
                self.logger.debug('Error: %r.', ex)
                self.logger.error("traceback: %r", traceback.format_exc())
                click.secho(ex.msg, fg='red')
            except DockerPermissionException as ex:
                self.logger.debug('Permission exception: %r.', ex)
                self.logger.error("traceback: %r", traceback.format_exc())
                click.secho(ex.message, fg='red')
            except EOFError:
                break
            except Exception as ex:
                self.logger.debug('Exception: %r.', ex)
                self.logger.error("traceback: %r", traceback.format_exc())
                click.secho("{0}".format(ex), fg='red')
                break

        self.revert_less_opts()
        self.write_config_file()
        print('Goodbye!')
@click.command()
def cli():
    """
    Create and call the CLI
    """
    saltcli = SaltCli()
    saltcli.run_cli()

if __name__ == "__main__":
    cli()
