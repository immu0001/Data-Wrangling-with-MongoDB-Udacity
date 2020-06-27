#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"
import string
from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []

    with open(page, "r") as html:
      # do something here to find the necessary values
      soup = BeautifulSoup(html)

      for airport in soup.find(id="AirportList").find_all("option"):

        if string.find(airport['value'].lower(), 'all') != 0:
          data.append(airport['value'])

    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()