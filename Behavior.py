from PIL import Image


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

        if self.active_flag:
            self.sense_and_act()  # Update match_degree, motor_recommendations
            self.weight = self.match_degree * self.priority
            # Do stuff with weight and motor_recommendations
            raise NotImplementedError

    def sense_and_act(self):
        # Uses its sensobs and calculates match_degree, motor_recommendations
        # Implemented in each subclass
        raise NotImplementedError


class CameraColorBehavior(Behavior):
    """docstring for CameraColorBehavior."""
    def __init__(self, bbcon, sensobs, priority):
        super(CameraColorBehavior, self).__init__(bbcon, sensobs, priority)

    def consider_deactivation(self):
        if not self.bbcon.activate_camera:
            self.active_flag = False
            # May have to update lists of active behaviors and sensobs in bbcon

    def consider_activation(self):
        if self.bbcon.activate_camera:
            self.active_flag = True
            # May have to update lists of active behaviors and sensobs in bbcon

    def sense_and_act(self):
        img = self.sensobs[0].get_value()
        width, height = img.size
        for y in range(height):
            for x in range(width):
                img.getpixel((x,y))
