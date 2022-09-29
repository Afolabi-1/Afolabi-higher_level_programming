#!/usr/bin/python3

def search_replace(my_list, search, replace):
    lst = my_list[:]
    for x in range(len(my_list)):
        if lst[x] == search:
            lst[x] = replace
    return(lst) 
