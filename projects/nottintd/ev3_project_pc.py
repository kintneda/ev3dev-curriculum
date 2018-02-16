import ev3dev.ev3 as ev3
import time
import math
import robot_controller as robo
from PIL import Image
import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk

class MyDelegate(object):

def main():
    mqtt = com.MqttClient()
    mqtt.connect_to_ev3()

    # Everything for creating GUI
    root = tkinter.Tk()
    root.title("Burger Stand Menu")

    main_frame = ttk.Frame(root, padding=50)
    main_frame.grid()

    welcome_label = ttk.Label(main_frame, text="WELCOME TO ROBOT BURGERS", font=("Algerian", 20))
    welcome_label.grid(row=0, columnspan=2)
    burger_label = ttk.Label(main_frame, text="Burgers", font=("Helvetica", 16))
    burger_label.grid(row=1, columnspan=2)

    quarter_pounder_checkbutton = ttk.Checkbutton(main_frame, text="1/4 Pounder", offvalue=None,
                                                  onvalue="quarter pounder")
    quarter_pounder_checkbutton.grid(row=2, column=0, sticky="W")
    quarter_pounder_value = tkinter.StringVar()
    quarter_pounder_checkbutton['variable'] = quarter_pounder_value

    half_pounder_checkbutton = ttk.Checkbutton(main_frame, text="1/2 Pounder", onvalue="half pounder")
    half_pounder_checkbutton.grid(row=2, column=1, sticky="W")
    half_pounder_value = tkinter.StringVar()
    half_pounder_checkbutton['variable'] = half_pounder_value

    cheeseburger_checkbutton = ttk.Checkbutton(main_frame, text="Cheeseburger", onvalue="cheeseburger")
    cheeseburger_checkbutton.grid(row=3, column=0, sticky="W")
    cheeseburger_value = tkinter.StringVar()
    cheeseburger_checkbutton['variable'] = cheeseburger_value

    double_cheeseburger_checkbutton = ttk.Checkbutton(main_frame, text="Double Cheeseburger",
                                                      onvalue="double cheeseburger")
    double_cheeseburger_checkbutton.grid(row=3, column=1, sticky="W")
    double_cheeseburger_value = tkinter.StringVar()
    double_cheeseburger_checkbutton['variable'] = double_cheeseburger_value

    fries_label = ttk.Label(main_frame, text="Fries", font=("Helvetica", 16))
    fries_label.grid(row=4, columnspan=2)

    small_fries_checkbutton = ttk.Checkbutton(main_frame, text="Small", onvalue="small fries")
    small_fries_checkbutton.grid(row=5, column=0, sticky="W")
    small_fries_value = tkinter.StringVar()
    small_fries_checkbutton['variable'] = small_fries_value

    medium_fries_checkbutton = ttk.Checkbutton(main_frame, text="Medium", onvalue="medium fries")
    medium_fries_checkbutton.grid(row=5, column=1, sticky="W")
    medium_fries_value = tkinter.StringVar()
    medium_fries_checkbutton['variable'] = medium_fries_value

    large_fries_checkbutton = ttk.Checkbutton(main_frame, text="Large", onvalue="large fries")
    large_fries_checkbutton.grid(row=6, column=0, sticky="W")
    large_fries_value = tkinter.StringVar()
    large_fries_checkbutton['variable'] = large_fries_value

    drinks_label = ttk.Label(main_frame, text="Drinks", font=("Helvetica", 16))
    drinks_label.grid(row=7, columnspan=4)

    water_checkbutton = ttk.Checkbutton(main_frame, text="Water", onvalue="water")
    water_checkbutton.grid(row=8, column=0, sticky="W")
    water_value = tkinter.StringVar()
    water_checkbutton['variable'] = water_value

    soda_checkbutton = ttk.Checkbutton(main_frame, text="Soda", onvalue="Soda")
    soda_checkbutton.grid(row=8, column=1, sticky="W")
    soda_value = tkinter.StringVar()
    soda_checkbutton['variable'] = soda_value

    juice_checkbutton = ttk.Checkbutton(main_frame, text="Juice", onvalue="juice")
    juice_checkbutton.grid(row=9, column=0, sticky="W")
    juice_value = tkinter.StringVar()
    juice_checkbutton['variable'] = juice_value

    coffee_checkbutton = ttk.Checkbutton(main_frame, text="Coffee", onvalue="coffee")
    coffee_checkbutton.grid(row=9, column=1, sticky="W")
    coffee_value = tkinter.StringVar()
    coffee_checkbutton['variable'] = coffee_value

    order_button = ttk.Button(main_frame, text="Order")
    order_button.grid(row=10, columnspan=2)
    order_button['command'] = lambda: get_order(quarter_pounder_value, half_pounder_value, cheeseburger_value,
                                                double_cheeseburger_value, small_fries_value, medium_fries_value,
                                                large_fries_value, water_value, soda_value, juice_value, coffee_value)
    root.mainloop()

#     END OF GUI


def get_order(quarter_pounder_value, half_pounder_value, cheeseburger_value, double_cheeseburger_value,
              small_fries_value, medium_fries_value,large_fries_value,
              water_value, soda_value, juice_value, coffee_value):
    rough_order = [quarter_pounder_value.get(), half_pounder_value.get(), cheeseburger_value.get(),
                        double_cheeseburger_value.get(), small_fries_value.get(), medium_fries_value.get(),
                        large_fries_value.get(), water_value.get(), soda_value.get(), juice_value.get(),
                        coffee_value.get()]
    print(rough_order)
    your_order = []
    for k in range(len(rough_order)):
        if len(rough_order[k]) > 0:
            your_order = your_order + [rough_order[k]]
    print(your_order)

    ev3.Sound.speak("Your order is a").wait()
    for k in range(len(your_order)):
        ev3.Sound.speak(your_order[k]).wait()

    for k in range(len(your_order)):
        if your_order[k] == "quarter pounder" or "half pounder" or "cheeseburger" or "double cheeseburger":
            mqtt.send_message("make_burger")
        if your_order[k] == "small fries" or "medium fries" or "large fries":
            mqtt.send_message("get_fries")
        if your_order[k] == "water" or "soda" or "juice" or "coffee":
            mqtt.send_message("get_drink", )


main()