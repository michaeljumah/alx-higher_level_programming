#!/usr/bin/python3
"""Takes in a letter and sends a POST request
to `http://0.0.0.0:5000/search_user` with the
letter as a parameter and with `requests` module.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        adict = {'q': ''}
    elif len(sys.argv) > 1:
        adict = {'q': sys.argv[1]}

    try:
        request = requests.post('http://0.0.0.0:5000/search_user', adict)
        if request.json():
            print('[{}] {}'.format(request.json().get('id'),
                                   request.json().get('name')))
        else:
            print('No result')

    except ValueError:
        print("Not a valid JSON")
