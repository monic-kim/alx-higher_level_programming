#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sen_len = 0
        first_char = 0
    else:
        sen_len = len(sentence)
        first_char = sentence[0]
    return sen_len, first_char
