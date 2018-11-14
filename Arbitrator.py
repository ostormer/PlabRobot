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


class Arbitrator:

    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self, weighted_random=False):
        behaviors = self.bbcon.active_behaviors
        recommendations, weights = [], []
        for b in behaviors:
            recommendations.append(b.motor_recommendations)
            weights.append(b.weight)
            print("Appended " + str(recommendations[-1]) + str(weights[-1]))
        chosen = None

        if weighted_random:
            chosen = weightedChoice(recommendations, weights)
        else:
            chosen = max(zip(weights, recommendations))[1]

        return chosen
