#!/bin/bash
#sends a POST request to the URL, and displays body of the response.
curl -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
