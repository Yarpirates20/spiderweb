"""
DESCRIPTION
===========

This module contains web scraping and network helper functions. 

MODULE CONTENTS
===============

getHTML(url, commentsOnly=False)


EXAMPLES
========

#TODO: write examples

"""

from bs4 import BeautifulSoup as BS
from bs4 import Comment
from bs4 import MarkupResemblesLocatorWarning
import requests
import warnings


def getHTML(url: str, commentsOnly: bool = False, robots: bool = False) -> BS:
    """ Parses HTML of web page with option of only returning comments """
    if robots:
        url = f"{url}/robots.txt"
        warnings.filterwarnings('ignore', category=MarkupResemblesLocatorWarning)

    res = requests.get(url)
    res.raise_for_status()
    page = BS(res.content, 'html.parser')

    if commentsOnly:
        comments = page.find_all(string=lambda text: isinstance(text, Comment))
        return comments
    else:
        return page.prettify()


#---------------------------------------------

# if __name__ == '__main__':
#     main()
