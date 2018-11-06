from Arbitrator import *
from Behavior import *
from zumo_button import ZumoButton
from time import sleep
from Motob import *

class BBCON:
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.inactive_behaviors = []
        self.sensobs = []
        self.motobs = Wheels() #gidder ikke bruke en liste her, hvor mange hjul har dere tenkt å ha??
        self.arbitrator = Arbitrator(self)
        #Legger til sensorene vi ønsker å bruke
        self.add_behavior(UV_behavior(self))
        self.add_behavior(camera_behavior(self))
        self.add_behavior(proximity_behavior(self))
        #Looper gjennom alle behaviors for å legge til alle sensorene som trengs for behaviors
        for behavior in self.behaviors:
            if behavior.sensobs not in self.sensobs:
                self.add_sensob(behavior.sensobs)


    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.pop(behavior)

    def run_one_timestep(self):
        for sensob in self.sensobs:
            sensob.update() #Sjekker alle sensorer
        for behavior in self.behaviors:
            behavior.update() #Fikser noe på behavior, spørr behavior mennesket (Solveig), hun ville ha det her
        self.motobs.update(self.arbitrator.choose_action().motor_rec)  #Oppdaterer hvordan hjula skal handle utifra hvordan arbitrator ønsker det
        sleep(0.5)
        for sensob in self.sensobs:
            sensob.reset() #reseter alt igjen så ikke noe fucker seg opp

def main():
    bbcon = BBCON()
    wheels = Wheels()
    print(wheels.motors[0])
    wheels.motors[0].forward(0.4,10)
    #ZumoButton().wait_for_press()
    while True: #Dette blir loopen som kjører evig helt til vi skår av Bernt.
        bbcon.motobs.motors[0].set_value([1,1])
        print("Trying forward")
        bbcon.run_one_timestep()
        bbcon.motobs.update([('FORWARD', 0.4, 0.6)])

main()