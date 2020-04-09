#!/bin/bash
#displays all HTTP methods the server will accept.
curl -sI ALLOW "$1" | grep "Allow" | cut -d " " -f2-
