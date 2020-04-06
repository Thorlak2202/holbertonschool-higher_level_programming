#!/bin/bash
curl -sI GET "$1" | awk '/Content-Length/{print $2}'