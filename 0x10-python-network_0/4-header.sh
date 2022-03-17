#!/usr/bin/bash
# Sends a GET rqst and displays the body of the response
curl -H "X-School-User-Id:98" -XLs GET "$1"
