#!/usr/bin/python3
import json
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'
if os.path.exists(filename):
    N_list = load_from_json_file(filename)
else:
    N_list = []
for i in range(1, len(sys.argv)):
    N_list.append(sys.argv[i])
save_to_json_file(N_list, filename)
