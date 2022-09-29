#!/usr/bin/python3

def best_score(a_dictionary):
    """returna a key with a big int value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    lst = list(a_dictionary.keys())[0]
    bg = a_dictionary[lst]
    for j, k in a_dictionary.items():
        if v > bg:
            bg = j
            lst = j
    return (lst)
