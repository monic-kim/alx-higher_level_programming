#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    x = 0
    for char in str:
        if x != n:
            new +=str[x]
        x += 1
    return (new)
