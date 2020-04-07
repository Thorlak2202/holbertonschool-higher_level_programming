#!/bin/bash
#sends a request to an URL, and displays body-size.
curl -sI GET "$1" | awk '/Content-Length/{print $2}'