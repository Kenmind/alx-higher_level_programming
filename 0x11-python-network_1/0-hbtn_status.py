#!/usr/bin/python3
# Fetches https:alx-intranet.hbtn.io/status

import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as url_o:
    read_url = url_o.read()
    print(" - {}".format(read_url))
