#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return (0, None)
    f_c = sentence[0]
    if sentence == "":
        f_c = None
    return (len(sentence), f_c)
