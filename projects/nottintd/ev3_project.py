import ev3dev.ev3 as ev3
import time
import math
import robot_controller as robo
from PIL import Image
import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk


def main():
    # arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
    # assert arm_motor.connected
    # left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    # assert left_motor.connected
    # right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    # assert right_motor.connected
    # touch_sensor = ev3.TouchSensor()
    # assert touch_sensor
    # mqtt_client = com.MqttClient()
    # mqtt_client.connect_to_ev3()
    # robot = robo.Snatch3r()
    root = tkinter.Tk()
    #Create a title
    root.wm_title('Checkbutton!')
    #Create a canvas
    drawpad = Canvas(
    root, background='white')
    drawpad.grid(row=0, column=1)
    root.mainloop()

main()