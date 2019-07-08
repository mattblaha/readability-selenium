#!/usr/bin/env python

from readability import Reader

from selenium import webdriver

import sys

driver = webdriver.Remote(
  command_executor='http://localhost:4444/wd/hub',
  desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})


# to supply a full path to Readability.js, do this
#js = open("/tmp/Readability.js").read()
#r = Reader(driver, readability_js=js)

r = Reader(driver)

url = sys.argv[1]
a = r.get_url(url)

print(a)

