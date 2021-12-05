#!/usr/bin/env python3

from readability_selenium import Reader

from selenium import webdriver

import sys

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.headless = True

driver = webdriver.Remote(
  command_executor='http://localhost:4444/wd/hub',
  desired_capabilities=options.to_capabilities())

# to supply a full path to Readability.js, do this
#js = open("/tmp/Readability.js").read()
#r = Reader(driver, readability_js=js)

r = Reader(driver)

url = sys.argv[1]
a = r.get_readable_dict(url)

print(a['content'])
print(a['byline'])

