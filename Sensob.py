class Sensob:
    """Parent method for Sensobs
    Calls Sensor objects' methods to get their values, used by Behaviors
    I think the best way to implement sensobs that process input data
    is as individual subclasses.
    This class works for simple sensobs that read raw sensor data"""

    def __init__(self, sensors):
        self.sensors = sensors  # A list(!) of sensors used by the sensobs
        self.value = [None] * len(self.sensors)  # Value(s) of the Sensob. Updated by update() method
        self.active_flag = True

    def update(self):
        if self.active_flag:
            self.value = []
            for sens in self.sensors:
                # Need to double-check that this works in all sensor wrappers
                sens.update()
                self.value.append(sens.get_value())

    def get_value(self):
        return self.value
