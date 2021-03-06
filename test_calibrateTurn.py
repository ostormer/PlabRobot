from basic_robot.zumo_button import ZumoButton
from Motob import Motob
from basic_robot.motors import Motors
from time import sleep


mtr = Motors()
mtb = Motob(mtr)

btn = ZumoButton()

while True:
    btn.wait_for_press()
    sleep(1)
    print("Turning 360 deg left")
    mtr.left(speed=0.7, dur=360/135)
    btn.wait_for_press()
    sleep(1)
    mtr.right(speed=0.7, dur=360/120)

# mtb.recom = ("L", 360)
# mtb.operationalize()
