

class Behavior:
    """A behavior of the BBR"""
    def __init__(self, bbcon, sensobs, priority):
        self.bbcon = bbcon  # Pointer to the controller
        self.sensobs = sensobs  # A list of sensobs this behavior uses
        self.priority = priority  # Constant, pre-defined priority of this behavior
        # A list of recommendations that this behavior provides to the arbitrator.
        self.motor_recommendations = None
        self.active_flag = False
        self.halt_request = False
        # match degree in range [0,1] indicates how important it is to run this behavior
        self.match_degree = 0
        self.weight = 0  # Product of priority and match_degree

    def consider_activation(self):
        # when a behavior is active it should test whether it should deactivate
        raise NotImplementedError

    def consider_deactivation(self):
        # when a behavior is inactive it should test whether it should activate
        raise NotImplementedError

    def update(self):
        # Called by the BBCON
        if self.active_flag:
            self.active_flag != self.consider_deactivation()
        else:
            self.active_flag == self.consider_activation()
        if not self.active_flag:
            # Deactivate
            raise NotImplementedError

        self.sense_and_act()  # Update match_degree, motor_recommendations
        self.weight = self.match_degree * self.priority
        # Do stuff with weight and motor_recommendations
        raise NotImplementedError

    def sense_and_act(self):
        # Uses its sensobs and calculates match_degree, motor_recommendations

        raise NotImplementedError
