#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if x > 0:
        y = sentence[0]
    else:
        y = None
    return (x, y)
    