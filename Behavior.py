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
        pass

    def consider_deactivation(self):
        # when a behavior is inactive it should test whether it should activate
        pass

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
    """Behavior subclass that should determine the color the camera sees the most of."""

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
        col = [0, 0, 0]
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                col[0] += r
                col[1] += g
                col[2] += b

        tot = sum(col)
        frac = [c / tot for c in col]
        print(frac)


class IR(Behavior):

    def sense_and_act(self):
        value = self.sensobs.get_value()

        dark_treshold = 0.25
        readings = self.update()
        dark_count = 0
        reflect_sum = 0
        for reflectance in readings:
            if reflectance < dark_treshold:
                dark_count += 1
                reflect_sum += reflectance
        # Update match_degree and weight
        if dark_count >= 2:  # Need at least 2 dark readings to have any priority
            self.match_degree = 0.5 + 0.5 * (1 - reflect_sum / dark_count)
        else:
            self.match_degree = 0
        # Update motor_recommendations
        self.motor_recommendations = (("L", 180))  # Turn 180 deg



class UltrasonicBehavior(Behavior):
