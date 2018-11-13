from basic_robot.zumo_button import ZumoButton
from Motob import Motob
from basic_robot.motors import Motors
from time import sleep


mtr = Motors()
mtb = Motob(mtr)

mtb.recom = ("L", 180)

btn = ZumoButton()
btn.wait_for_press()
sleep(4)
mtb.operationalize()
