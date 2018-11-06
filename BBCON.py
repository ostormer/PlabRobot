from time import sleep
from Arbitor import Arbitor

class BBCON:

    def __init__(self):
        self.behaviors = []  # list of all behaviors
        self.active_behaviors = []  # list of all active behaviors
        self.sensobs = []  # list of all sensory objects used by the bbcno
        self.motobs = []  # list of all motors objects used by the bbcon
        self.arbitrator = Arbitrator()# arbitrator object that will resolve actuator requests produced by the behaviors
        # ikke lagt til forslag om timestep, inactive o.l.

    # metoder for bbcon
    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def activate_behavior(self, behavior):
        if behavior not in self.behaviors:
            raise Exception("maa ha adferden som forsokes aktivert")
        self.active_behaviors.append(behavior)

    def deactive_behavior(self, behavior):
        self.active_behaviors.remove(behavior)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    # mainmetode/kjerneaktivitet i bbcon
    def run_one_timestep(self):
        self.update_all_sensobs()  # 1. oppdater alle sensobs
        self.update_all_behaviors()  # 2. oppdater alle behaviors
        #motor rec er en liste
        motor_recommendations = self.arbitrator.choose_action()  # 3. invoke arbitrator by caling choose action, mellomlagre output
        self.update_motobs(motor_recommendations)  # 4.update settings of all motors
        self.wait(0.5)  # 5. pause for å la motorsettings være aktive en periode
        self.reset_sensobs()  # 6.

    # støttefunksjoner til run_one_timestep
    def update_all_sensobs(self):
        raise NotImplementedError

    def update_all_behaviors(self):
        raise NotImplementedError

    def update_motobs(self, recommendations):
        #tar inn en liste av recommendations 
        raise NotImplementedError

    def wait(self, seconds):
        sleep(seconds)  # står eksempelvis halvt sek,må sikkert justeres

    def reset_sensobs(self):
        raise NotImplementedError
        