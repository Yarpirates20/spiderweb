"""
DESCRIPTION
===========

This module contains vulnerability test helper functions. 

MODULE CONTENTS
===============



EXAMPLES
========

#TODO: write examples

"""

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs, ResultSet
from urllib.parse import urljoin

def get_all_forms(url: str) -> ResultSet:
    """ Gets all forms from a url """
    soup = bs(requests.get(url).content, 'html.parser')
    return soup.find_all("form")

def get_form_details(form: bs) -> dict:
    """ Returns dictionary of form details. """
    form_details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "test")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})

    form_details["action"] = action
    form_details["method"] = method
    form_details["inputs"] = inputs

    return form_details

if __name__ == "__main__":
    url = "http://testphp.vulnweb.com"
    forms = get_all_forms(url)
    form_details = []

    print(forms)
    print(type(forms))

    for i in forms:
        print(get_form_details(i))
    # for i in form_details:
    #     for k, v in i:
    #         print(f"{k} : {v}")
