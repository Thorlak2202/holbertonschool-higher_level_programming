#!/bin/bash
#sends a request to an URL, and displays body-size.
curl -sI GET "$1" | grep "Content-Length" | cut -d " " -f2-
