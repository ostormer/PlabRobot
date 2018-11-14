from basic_robot.motors import Motors


class Motob:
    """Motor object that handles motor motor_recommendations
    and sends them to the right motors"""

    def __init__(self, motors):
        self.motors = motors  # A Motors object used by the Motob
        # Value(s) of the Motob. Received and handled in the update() method
        self.recom = None

    def update(self, recommendation):
        # First receive the correct recommendation here:
        self.recom = recommendation
        self.operationalize()  # Then operationalize it

    def operationalize(self):
        # Motor recommendations are in the format "Command", value)
        # for example: ("L", 30) : means turn 30 deg to the left
        # or ("F", [2, 0.3]) : means drive forward for 2 sec at 0.3 speed
        command, value = self.recom[0], self.recom[1:]
        if command == "L":
            # Turn left degrees
            dur = value[0]/135
            self.motors.left(speed=0.7, dur=dur)
        elif command == "R":
            # Turn right degrees
            dur = value[0]/120
            self.motors.right(speed=0.7, dur=dur)
        elif command == "F":
            # Drive forward seconds
            self.motors.forward(speed=0.5, dur=value[0])
        elif command == "R":
            # Reverse seconds
            self.motors.backward(speed=0.5, dur=value[0])
        elif command == "WAIT":
            # wait seconds
            self.motors.stop()
            self.motors.persist(value[0])
