#!/usr/bin/python3
"""Fetches the URL: https://intranet.hbtn.io/status
with `requests` module
"""
import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    request = "Body response:\n\t- type: {}\n\t- content: {}"
    print(request.format(type(response.text), response.text))
