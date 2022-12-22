#!/usr/bin/python3
def no_c(my_string):
    replace_str = ""
    for elm in my_string:
        if elm != 'C' and elm != 'c':
            replace_str += elm
    return replace_str
