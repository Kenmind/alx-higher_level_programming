#!/bin/bash
# Sends a POST rqst and displays the body of the response
curl -ds "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
