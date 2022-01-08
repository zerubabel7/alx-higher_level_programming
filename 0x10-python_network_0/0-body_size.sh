#!/usr/bin/env bash
# Takes in a URL
# sends a request to that URL
# displays the size of the response body
curl -s "$1" | wc -c