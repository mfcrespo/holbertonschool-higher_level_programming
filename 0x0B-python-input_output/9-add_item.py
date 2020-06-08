#!/usr/bin/python3
""" My Module that reads json data then adds to it
"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
with open(filename, "a", encoding="UTF-8") as f:
    try:
        my_list = load_from_json_file(filename)
    except:
        my_list = []
    for arg in range(1, len(argv)):
        my_list += [argv[arg]]
    save_to_json_file(my_list, filename)
