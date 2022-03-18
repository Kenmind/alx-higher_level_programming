#!/usr/bin/python3
"""
    Sends a POST request and displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    email = {"email:"sys.argv[2]}
    url = sys.argv[1]
    post = requests.post(url, {"email:" data=email})
    print(post.text)
