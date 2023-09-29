#!/usr/bin/python3
"""Fetches the URL: https://intranet.hbtn.io/status
"""
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as url:
    d = url.read()
    request = "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
    print(request.format(type(d), d, d.decode('utf-8')))
