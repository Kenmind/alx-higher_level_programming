#!/bin/bash
# Sends a POST rqst from a JSON file and displays the body of the response
curl -ds -T"$2" -X POST "$1"
