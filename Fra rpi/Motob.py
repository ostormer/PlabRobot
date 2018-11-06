from motors import *

class Motob:

    def __init__(self):
        self.motors = [Motors()]
        self.value = None

    def update(self, rec):
        pass

    def operationalize(self):
        pass


class Wheels(Motob):
    def __init__(self):
        super().__init__()


    def update(self, rec):
        self.value = rec
        self.operationalize()

    def operationalize(self):
        print(self.value)
        for i in range(len(self.value)):
            print(self.value[i][0])
            if self.value[i][0] == 'FORWARD':
                self.motors[0].forward(self.value[i][1], self.value[i][2]) #(fart, tid)
            elif self.value[i][0] == 'BACKWARD':
                self.motors[0].backward(self.value[i][1], self.value[i][2])
            elif self.value[i][0] == 'STOP':
                self.motors[0].stop()
            elif self.value[i][0] == 'RIGHT':
                self.motors[0].right(self.value[i][1], self.value[i][2])
            elif self.value[i][0] == 'LEFT':
                self.motors[0].left(self.value[i][1], self.value[i][2])

