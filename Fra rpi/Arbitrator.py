

class Arbitrator():

    def __init__(self, bbcon):
        self.bbcon = bbcon


    def choose_action(self):
        max = self.bbcon.active_behaviors[0].weight
        winner = self.bbcon.active_behaviors[0]
        for behavior in self.bbcon.active_behaviors:
            if behavior.weight > max:
                max = behavior.weight
                winner = behavior
        return winner


