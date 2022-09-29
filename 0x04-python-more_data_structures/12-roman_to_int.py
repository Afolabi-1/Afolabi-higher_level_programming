#!/usr/bin/python3
# 12-roman_to_int.py


def roman_to_int(roman_string):
    """Convert roman numeral to int."""
    if roman_string != str(roman_string):
        return (0)
    if roman_string is None:
        return (0)

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0
    r_dict = roman_dict

    for j in range(len(roman_string)):
        if r_dict.get(roman_string[j], 0) == 0:
            return (0)

        if (j != (len(roman_string) - 1) and r_dict[roman_string[j]] < r_dict[roman_string[j + 1]]):
                num += r_dict[roman_string[j]] * -1
        else:
            num += r_dict[roman_string[j]]
    return (num)
