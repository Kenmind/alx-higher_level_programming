#!/bin/bash
# Sends a POST rqst from a JSON file and displays the body of the response
curl -Xs POST -H "Content-type:application/json" -d @"$2" "$1"
