#!/usr/bin/python3

def roman_to_int(roman_string):
    # Fail checks, none, not a string
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    roman_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        "X": 10,
        "VII": 7,
        "IX": 9,
        "LXXXVII": 87,
        "DCCVII": 707,
    }
    result = 0
    temp = list(roman_string)
    # Concat 4 and 9s
    if len(temp) > 1:
        idx = 0
        for i in temp:
            try:
                if temp[idx] == 'I' and temp[idx + 1] == 'V':
                    temp[idx:idx + 2] = [''.join(temp[idx:idx + 2])]
            except IndexError:
                pass
            try:
                if temp[idx] == 'I' and temp[idx + 1] == 'X':
                    temp[idx:idx + 2] = [''.join(temp[idx:idx + 2])]
            except IndexError:
                pass
            idx += 1
    # Search in dict for correct numbers and add
    for k, v in r_dict.items():
        for index in temp:
            if index == k:
                result += v
    return result
