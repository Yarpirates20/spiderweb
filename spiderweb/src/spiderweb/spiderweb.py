#!/usr/bin/env python3

import argparse
from typing import List
from Commands import Command, Get, Guide
import sys

def getOptions(argv: List[str] = sys.argv[1:]) -> argparse.Namespace:
    """ Parse the command-line options. """
    parser = argparse.ArgumentParser(prog="spiderweb")
    subparsers = parser.add_subparsers()

    getSubparser = subparsers.add_parser("get")
    getSubparser.set_defaults(func=Get)
    Get.arguments(getSubparser)


    guideSubparser = subparsers.add_parser("guide")
    guideSubparser.set_defaults(func=Guide)
    Guide.arguments(guideSubparser)

    return parser.parse_args(argv)

def main() -> None:
    """ The main entry point for the spiderweb CLI. """
    options = getOptions(sys.argv[1:])
    command = options.func
    command.execute(command, options)



if __name__ == "__main__":
    main()