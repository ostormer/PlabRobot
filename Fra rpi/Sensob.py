from irproximity_sensor import IRProximitySensor
from camera import Camera
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton
from time import sleep
import RPi.GPIO as GPIO

class Sensob:

    #serves as an interface between one or more sensors and bbcon behav
    def __init__(self):
        self.sensors = []
        self.value = None

    def get_value(self):
        return self.value

    def update(self):
        return

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()


class Proximity(Sensob):

    def __init__(self):
        self.sensors = IRProximitySensor()
        self.value = None

    def get_value(self):
        # True means something is close
        # Boolean array, with one value for each sensor
        return self.value

    def reset(self):
        self.sensors.reset()

    def update(self):
        self.sensors.update()
        self.value = self.sensors.get_value()



class CameraSensob(Sensob):

    #kamera, skal detektere farge og analysere
    def __init__(self, threshold, CR):  #0.4, (0.5, 0.25, 0, 0.25)
        self.threshold = threshold
        self.CR = CR                #hvor mye av bildet skal være med?
        self.sensors = Camera()
        self.value = []
        self.values = [0,0,0]


    def update(self):
        image = self.sensors.update()
        width, height = image.size

        for h in range(height):
            for w in range(width):
                pixel = image.getpixel((w, h))
                image.putpixel((w, h), self.largest_pixel(pixel))


        num_pixels = [0,0,0]

        for w in range(width):
            for h in range(height):
                pixel = list(image.getpixel((w,h)))
                num_pixels[pixel.index(1)] += 1

        color_fraction = [0.0, 0.0, 0.0]
        pixel_amount = width*height
        for i in range(len(num_pixels)):
            color_fraction[i] = num_pixels[i] / pixel_amount

        self.value = color_fraction

    def largest_pixel(self, pixels):
        width = max(pixels)
        lenght = list(pixels)
        index = lenght.index(width)
        values = [0, 0, 0]
        values[index] = 1
        return tuple(values)

    def get_value(self):
        return self.value

    def reset(self):
        self.sensors.reset()


class UV(Sensob):

    def __init__(self):
        self.sensors = Ultrasonic()

    def update(self):
        self.sensors.update()
        self.value = self.sensors.get_value()

    def get_value(self):
        return self.value

    def reset(self):
        self.sensors.reset()


def main():
    try:
        p = Proximity()
        u = UV()
        c = CameraSensob()
        zb = ZumoButton()
        while True:    
            p.update()
            u.update()
            c.update()
            print("Camera: ", c.get_value())
            print("Proximity: ", p.get_value())
            print("UV: ", u.get_value())
            sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
        main()