"""
Description
===========

This module contains the commands that can be executed by the spiderweb CLI.

Module Contents
===============

    * Command: The base class for all commands.

Examples
========

    * Example 1: Creating a new command.

"""

import argparse
from pprint import pprint
import requests
import sys
from typing import List

class Command:
    """ The base class for all commands. """
    @classmethod
    def arguments(cls, subparser: argparse.ArgumentParser) -> None:
        """ Add command-specific arguments to the subparser. """
        pass

    def __init__(self) -> None:
        pass

    def execute(self, options: argparse.Namespace) -> None:
        """ Execute the command. """
        pass

class Get(Command):
    """ The get command. """
    @classmethod
    def arguments(cls, getSubparser: argparse.ArgumentParser) -> None:
        getSubparser.add_argument(
            "url",
            type=str,
            help="The URL to fetch."
        )

        getSubparser.set_defaults(command=cls)

    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, options: argparse.Namespace) -> None:
        response = requests.get(options.url)
        pprint(response.text)
