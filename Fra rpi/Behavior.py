from Sensob import *


class Behavior(object):
    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensobs = None
        self.motor_rec = []
        self.active_flag = False
        self.halt_request = False
        self.priority = 1.0
        self.match_degree = 0
        self.weight = 0

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def sense_and_act(self):
        pass

    def weight_update(self):
        self.weight = self.priority * self.match_degree

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()
        self.sense_and_act()
        self.weight_update()


class UV_behavior(Behavior):
    def __init__(self, bbcon):
        super(UV_behavior, self).__init__(bbcon)
        self.sensobs = UV()
        self.active_flag = True
        self.bbcon.active_behaviors.append(self)

    def sense_and_act(self):
        distance = self.sensobs.get_value()
        if distance >= 10:
            self.bbcon.camera_activate = False
            self.motor_rec = [('FORWARD', 0.4, 0.6)]
            self.match_degree = 0.6
            self.weight_update()
        else:
            self.bbcon.camera_activate = True
            self.motor_rec = [('STOP', 0, 0)]
            self.match_degree = 0.3
            self.weight_update()


class camera_behavior(Behavior):

    def __init__(self, bbcon):
        super().__init__(bbcon)
        self.active_flag = True
        self.sensobs = CameraSensob(0.4, (0.5, 0.25, 0, 0.25))
        self.bbcon.active_behaviors.append(self)

    def consider_deactivation(self):
        if self.bbcon.camera_activate:
            self.active_flag = True
        else:
            self.active_flag = False
            self.bbcon.active_behaviors.pop(self.bbcon.active_behaviors.index(self))

    def consider_activation(self):
        if self.bbcon.camera_activate:
            self.active_flag = True
            if self not in self.bbcon.active_behaviors:
                self.bbcon.active_behaviors.append(self)
        else:
            self.active_flag = False

    def sense_and_act(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            fraction = self.sensobs.get_value()
            index = fraction.index(max(fraction)) #finn den fargen det er mest av
            if max(fraction) > 0.8:
                if index == 0:  #fargen er rod
                    self.motor_rec = [('FORWARD', 0.7, 1.0)]
                    self.match_degree = 0.5
                    self.weight_update()
                elif index == 1:  #fargen er gronn
                    self.motor_rec = [('BACKWARD', 0.2, 1.0)]
                    self.match_degree = 0.5
                    self.weight_update()
                else:  #fargen er blaa
                    self.motor_rec = [('RIGHT', 0.5, 1.0), ('FORWARD', 0.2, 1.0)]
                    self.match_degree = 0.5
                    self.weight_update()
            else:
                self.motor_rec = [('BACKWARD', 0.2, 0.5)]
                self.match_degree = 0.1
                self.weight_update()



class proximity_behavior(Behavior):
    def __init__(self, bbcon):
        super().__init__(bbcon)
        self.sensobs = Proximity()
        self.active_flag = True
        self.bbcon.active_behaviors.append(self)

    def sense_and_act(self):
        value = self.sensobs.get_value()
        if value[0] == True:
            self.motor_rec = [('RIGHT', 0.5, 1.5)]
            self.match_degree = 1
        elif value[1] == True:
            self.motor_rec = [('LEFT', 0.5, 1.5)]
            self.match_degree = 1
        else:
            self.motor_rec = [('STOP', 0.25, 1)]
            self.match_degree = 0