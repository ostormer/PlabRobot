from basic_robot.zumo_button import ZumoButton
from Motob import Motob
from basic_robot.motors import Motors
from time import sleep


mtr = Motors()
mtb = Motob(mtr)



btn = ZumoButton()
btn.wait_for_press()
sleep(2)
print("Turning 360 deg left")
mtb.recom = ("L", 360)
mtb.operationalize()
