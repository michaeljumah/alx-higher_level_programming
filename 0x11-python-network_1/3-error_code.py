#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
In addition, it handles HTTPError exceptions to print
the HTTP Status Code, if an error occurs.
"""
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as url:
            d = url.read()
            print(d.decode('utf-8'))
    except urllib.error.HTTPError as a:
        print("Error code: {}".format(a.code))
