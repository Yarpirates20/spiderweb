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
from guidedAttackTree import listSteps
from pprint import pprint
import requests
from scraping import getHTML
import sys
from typing import List

#------------------------------------------
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

#-----------------------------------------------------------------
class Get(Command):
    """ The get command. """
    @classmethod
    def arguments(cls, getSubparser: argparse.ArgumentParser) -> None:
        getSubparser.add_argument(
            "url",
            type=str,
            help="The URL to fetch."
        )

        getSubparser.add_argument(
            "-c",
            "--comments",
            action="store_true",
            default=False,
            help="Returns comments only"
        )

        getSubparser.add_argument(
            "-r",
            "--robots",
            action="store_true",
            default=False,
            help="Get robots.txt for URL"
        )

        getSubparser.set_defaults(command=cls)

    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, options: argparse.Namespace) -> None:
        page = getHTML(options.url, options.comments, options.robots)
        pprint(page)


#-----------------------------------------------------------------
class Guide(Command):
    """Step-by-step walkthrough for basic web app attacks. """
    @classmethod
    def arguments(cls, guideSubparser: argparse.ArgumentParser) -> None:
        guideSubparser.add_argument(
            "-i",
            "--interactive",
            action="store_true",
            default=False,
            help="Interactive mode"
        )

        guideSubparser.set_defaults(command=cls)

    def __init__(self) -> None:
        super().__init__()

    def execute(self, options: argparse.Namespace) -> None:
        listSteps()