#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    d_score = max(a_dictionary.values(), default=None)
    for d, w in a_dictionary.items():
        if w == d_score:
            return d
