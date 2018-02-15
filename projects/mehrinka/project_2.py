"""This is the final project for CSSE120, Introduction to Software Development. For this project, the robot can be
driven using keystrokes on the computer. When the up button on the ev3 is pressed, the robot sends back the color
sensed by the color sensor to the computer. The pc then interprets the data and prints an image in tkinter. The
robots imitates a tourist robot. Code was written primarily by Kyle Mehringer. Example code was used from Dave Fisher
in earlier modules and from Stack Overflow."""



import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
from tkinter import *
from PIL import ImageTk, Image

COLOR_NAMES = ["None", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
COLOR_NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7]


class DataContainer(object):
    """ Helper class that might be useful to communicate between different callbacks."""

    def __init__(self, root):
        self.root = root
        self.panel = None
        self.img = None
        self.running = True

    def on_color_received(self, color):
        print(COLOR_NAMES[color])

        if color == COLOR_NUMBERS[1]:
            print("Mountains")
            self.img = ImageTk.PhotoImage(Image.open("clingmans_dome1.png"))
            self.panel = Label(self.root, image=self.img)
            self.panel.grid()
        if color == COLOR_NUMBERS[2]:
            print("Lake")
            self.img = ImageTk.PhotoImage(Image.open("water.png"))
            self.panel = Label(self.root, image=self.img)
            self.panel.grid()


def main():

    root = Tk()
    root.title("Pictures")

    root.bind('<Up>', lambda event: drive_forward(mqtt_client, 500, 500))
    root.bind('<Left>', lambda event: turn_left(mqtt_client, 500, 500))
    root.bind('<space>', lambda event: stop(mqtt_client))
    root.bind('<Right>', lambda event: turn_right(mqtt_client, 500, 500))
    root.bind('<Down>', lambda event: drive_back(mqtt_client, 500, 500))
    root.bind('<u>', lambda event: send_up(mqtt_client))
    root.bind('<j>', lambda event: send_down(mqtt_client))

    my_delegate = DataContainer(root)
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_ev3()

    root.mainloop()


# ----------------------------------------------------------------------
# Tkinter callbacks
# ----------------------------------------------------------------------

def drive_forward(mqtt_client, left_speed_entry, right_speed_entry):
    print("drive_forward")
    mqtt_client.send_message("drive_forward", [int(left_speed_entry), int(right_speed_entry)])


def turn_left(mqtt_client, left_speed_entry, right_speed_entry):
    print("turn_left")
    mqtt_client.send_message("turn_left", [int(left_speed_entry), int(right_speed_entry)])


def stop(mqtt_client):
    print("stop")
    mqtt_client.send_message("stop")


def turn_right(mqtt_client, left_speed_entry, right_speed_entry):
    print("turn_right")
    mqtt_client.send_message("turn_right", [int(left_speed_entry), int(right_speed_entry)])


def drive_back(mqtt_client, left_speed_entry, right_speed_entry):
    print("drive_backward")
    mqtt_client.send_message("drive_backward", [int(left_speed_entry), int(right_speed_entry)])


# Arm command callbacks
def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


# Quit and Exit button callbacks
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
