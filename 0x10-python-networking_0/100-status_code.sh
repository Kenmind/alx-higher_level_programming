#!/usr/bin/bash
# Displays only the status code of an HTTP rqst
curl -s -o /dev/null -w "%{http_code}" "$1"
