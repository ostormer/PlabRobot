from time import sleep
from Arbitrator import Arbitrator
from Sensob import Sensob
from Motob import Motob
from Behavior import *
from basic_robot.motors import Motors
from basic_robot.ultrasonic import Ultrasonic
from basic_robot.reflectance_sensors import ReflectanceSensors
from basic_robot.camera import Camera
from basic_robot.zumo_button import ZumoButton


class BBCON:

    def __init__(self):
        self.behaviors = []  # list of all behaviors
        self.active_behaviors = []  # list of all active behaviors
        self.sensobs = []  # list of all sensory objects used by the bbcno
        self.motobs = []  # list of all motors objects used by the bbcon
        self.arbitrator = Arbitrator(self)  # arbitrator object that will resolve actuator requests produced by the behaviors
        self.activate_camera = False
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

    def add_motob(self, motob):
        self.motobs.append(motob)

    # mainmetode/kjerneaktivitet i bbcon
    def run_one_timestep(self):
        self.update_all_sensobs()  # 1. oppdater alle sensobs
        print("Updated all sensors")
        self.update_all_behaviors()  # 2. oppdater alle behaviors
        # motor rec er en liste
        motor_recommendations = [self.arbitrator.choose_action()]  # 3. invoke arbitrator by caling choose action, mellomlagre output
        print("Chosen recommendation: " + str(motor_recommendations))
        self.update_motobs(motor_recommendations)  # 4.update settings of all motors
        # self.wait(0.1)  # 5. pause for å la motorsettings være aktive en periode
        self.reset_sensobs()  # 6.

    # støttefunksjoner til run_one_timestep
    def update_all_sensobs(self):
        for sensob in self.sensobs:
            sensob.update()

    def update_all_behaviors(self):
        for behavior in self.behaviors:
            behavior.update()

    def update_motobs(self, recommendations):
        # tar inn en liste av recommendations, en for hver
        for motob, rec in zip(self.motobs, recommendations):
            motob.update(rec)

    def wait(self, seconds):
        sleep(seconds)  # står eksempelvis halvt sek,må sikkert justeres

    def reset_sensobs(self):
        for sensob in self.sensobs:
            sensob.value = [None] * len(sensob.sensors)
            for sensor in sensob.sensors:
                sensor.reset()


if __name__ == "__main__":


    bbcon = BBCON()
    bbcon.add_motob(Motob(Motors()))

    sens_ult = Sensob([Ultrasonic()])
    sens_ref = Sensob([ReflectanceSensors()])
    sens_cam = Sensob([Camera()])
    sens_cam.active_flag = False  # Camera starts deactivated
    bbcon.add_sensob(sens_ult)
    bbcon.add_sensob(sens_ref)
    bbcon.add_sensob(sens_cam)

    bbcon.add_behavior(UltrasonicBehavior(bbcon, [sens_ult], 0.5))
    bbcon.activate_behavior(bbcon.behaviors[0])
    bbcon.behaviors[0].active_flag = True
    bbcon.add_behavior(IR(bbcon, [sens_ref], 0.7))
    bbcon.activate_behavior(bbcon.behaviors[1])
    bbcon.behaviors[1].active_flag = True
    bbcon.add_behavior(CameraColorBehavior(bbcon, [sens_cam], 1))

    bbcon.motobs[0].motors.stop()

    btn = ZumoButton()
    btn.wait_for_press()
    sleep(2)
    bbcon.reset_sensobs()
    # Reset all sensors
    while True:
        bbcon.run_one_timestep()
