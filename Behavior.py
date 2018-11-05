

class Behavior:
    """A behavior of the BBR"""
    def __init__(self, bbcon, sensobs, motor_recommendations, priority):
        self.bbcon = bbcon  # Pointer to the controller
        self.sensobs = sensobs  # A list of sensobs this behavior uses
        # A list of recommendations that this behavior provides to the arbitrator.
        self.motor_recommendations = motor_recommendations
        self.priority = priority  # Constant, pre-defined priority of this behavior
        self.active_flag = False
        self.halt_request = False
        # match degree in range [0,1] indicates how important it is to run this behavior
        self.match_degree = 0
        self.weight = 0  # Product of priority and match_degree

    def consider_activation():
        # when a behavior is active it should test whether it should deactivate
        raise NotImplementedError

    def consider_deactivation():
        # when a behavior is inactive it should test whether it should activate
        raise NotImplementedError

    def update():
        # the main interface between the bbcon and the behavior
        raise NotImplementedError

    def sense_and_act():
        raise NotImplementedError
