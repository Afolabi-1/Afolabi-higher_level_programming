#!/usr/bin/python

def divisible_by_2(my_list=[]):
    even = []
    for int in range(len(my_list)):
        if my_list[int] % 2 == 0:
            even.append(True)
        else:
            even.append(False)
    return (
