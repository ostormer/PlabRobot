from basic_robot.motors import Motors


class Motob:
    """Motor object that handles motor motor_recommendations
    and sends them to the right motors"""

    def __init__(self, motors):
        self.motors = motors  # A Motors object used by the Motob
        # Value(s) of the Motob. Received and handled in the update() method
        self.recom = None

    def update(self):
        raise NotImplementedError
        # First receive the correct recommendation here:

        # Then operationalize it
        self.operationalize()

    def operationalize(self):
        # Motor recommendations are in the format "Command", value)
        # for example: ("L", 30) : means turn 30 deg to the left
        # or ("F", [2, 0.3]) : means drive forward for 2 sec at 0.3 speed
        command, value = self.recom[0], self.recom[1]
        print(command, value)
        if command == "L":
            # Turn left
            print("Turning left")
            dur = value/40  # SOME NUMBER WE NEED TO EXPERIMENT TO FIND
            self.motors.left(speed=0.25, dur=dur)
        elif command == "R":
            dur = value/40  # SOME NUMBER WE NEED TO EXPERIMENT TO FIND
            self.motors.right(speed=0.25, dur=dur)
        # More commands here...

        pass
