"""
DESCRIPTION
===========

This module contains helpers for guided walkthroughs. 

MODULE CONTENTS
===============




EXAMPLES
========

#TODO: write examples

"""
import cmd
from pprint import pprint
import requests
import shlex

class GuidedCLI(cmd.Cmd):
    intro = 'Web attack interactive guide'
    prompt = 'spiderweb> '

    def __init__(self, *args, **kwargs):
        super(GuidedCLI, self).__init__(*args, **kwargs)
        self.targetUrl = None

    def do_get  (self, url):
        r = requests.get(url)
        pprint(f"Head for: {url}\n {r.headers}")



if __name__ == "__main__":
    GuidedCLI().cmdloop()
    # listSteps()

# def listSteps() -> None:
#     print("\tDid you... ")
#     print("\t\tcheck the source code?")
#     print("\t\tcheck the comments?")
#     print("\t\tlook at robots.txt?")
