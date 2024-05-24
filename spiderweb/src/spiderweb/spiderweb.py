import argparse
from typing import List
from Commands import Command, Get
import sys

def getOptions(argv: List[str] = sys.argv[1:]) -> argparse.Namespace:
    """ Parse the command-line options. """
    parser = argparse.ArgumentParser(prog="spiderweb")
    subparsers = parser.add_subparsers()

    getSubparser = subparsers.add_parser("get")
    Get.arguments(getSubparser)

    return parser.parse_args(argv)

def main() -> None:
    """ The main entry point for the spiderweb CLI. """
    options = getOptions(sys.argv[1:])
    command = Get()
    command.execute(options)



if __name__ == "__main__":
    main()