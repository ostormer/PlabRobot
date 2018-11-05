from random import random


def weightedChoice(items, weights):
    if len(items) != len(weights):
        print("Wrong input")
        exit(0)

    c_weights = [0]
    for w in weights:
        c_weights.append(c_weights[-1] + w)
    r = random()*c_weights[-1]
    for i, cw in enumerate(c_weights):
        if r < cw:
            return items[i-1]
