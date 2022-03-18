#!/usr/bin/python3
# Sends a request to the URL and displays the value of the
#+ X-Request-Id variable found in the header of the response
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as url_o:
        print(url_o.info().get("X-Request-Id"))
