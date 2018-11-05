from random import random


def weightedChoice(items, weights):
    if len(items) != len(weights):
        print("Wrong input")
        exit(0)

    c_weights = [0]
    [c_weights.append(c_weights[-1] + w) for w in weights]
    r = random()*c_weights[-1]
    for i, cw in enumerate(c_weights):
        if r < cw:
            return items[i-1]


# ~~~~~~~~~~~~~~~~~~~TEST~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    items, weights = [3, 2, 10, 5], [.3, .2, 1.0, .5]
    counts = {3: 0, 2: 0, 10: 0, 5: 0}
    for i in range(200000):
        counts[weightedChoice(items, weights)] += 1

    print(counts)
