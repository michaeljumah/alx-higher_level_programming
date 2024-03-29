#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8).
"""
import urllib.request
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    hdata = urllib.parse.urlencode({"email": email}).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], hdata) as url:
        d = url.read()
        print(d.decode('utf-8'))
