#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        max_key = max(a_dictionary, key=lambda k: a_dictionary[k])
        return max_key
