

class Sensob:
    """Parent method for Sensobs
    I think making a subclass for each actual Sensob is the easiest solution"""

    def __init__(self, sensors):
        self.sensors = sensors  # A list(!) of sensors used by the sensobs
        self.value  # Value(s) of the Sensob. Updated by update() method

    def update():
        raise NotImplementedError
