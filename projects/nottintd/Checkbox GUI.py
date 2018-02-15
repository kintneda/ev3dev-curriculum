import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()
    root.title("Burger Stand Menu")

    main_frame = ttk.Frame(root, padding=50)
    main_frame.grid()

    welcome_label = ttk.Label(main_frame, text="WELCOME TO ROBOT BURGERS", font=("Algerian", 20))
    welcome_label.grid(row=0, columnspan=2)
    burger_label = ttk.Label(main_frame, text="Burgers", font=("Helvetica", 16))
    burger_label.grid(row=1, columnspan=2)

    quarter_pounder_checkbox = ttk.Checkbutton(main_frame, text="1/4 Pounder", offvalue=0, onvalue=1)
    quarter_pounder_checkbox.grid(row=2, column=0, sticky="W")

    half_pounder_checkbox = ttk.Checkbutton(main_frame, text="1/2 Pounder")
    half_pounder_checkbox.grid(row=2, column=1, sticky="W")

    cheeseburger_checkbox = ttk.Checkbutton(main_frame, text="Cheeseburger")
    cheeseburger_checkbox.grid(row=3, column=0, sticky="W")

    double_cheeseburger_checkbox = ttk.Checkbutton(main_frame, text="Double Cheeseburger")
    double_cheeseburger_checkbox.grid(row=3, column=1, sticky="W")

    fries_label = ttk.Label(main_frame, text="Fries", font=("Helvetica", 16))
    fries_label.grid(row=4, columnspan=2)

    small_fries_checkbutton = ttk.Checkbutton(main_frame, text="Small")
    small_fries_checkbutton.grid(row=5, column=0, sticky="W")

    medium_fries_checkbutton = ttk.Checkbutton(main_frame, text="Medium")
    medium_fries_checkbutton.grid(row=5, column=1, sticky="W")

    large_fries_checkbutton = ttk.Checkbutton(main_frame, text="Large")
    large_fries_checkbutton.grid(row=6, column=0, sticky="W")

    drinks_label = ttk.Label(main_frame, text="Drinks", font=("Helvetica", 16))
    drinks_label.grid(row=7, columnspan=4)

    water_checkbutton = ttk.Checkbutton(main_frame, text="Water")
    water_checkbutton.grid(row=8, column=0, sticky="W")

    soda_checkbutton = ttk.Checkbutton(main_frame, text="Soda")
    soda_checkbutton.grid(row=8, column=1, sticky="W")

    juice_checkbutton = ttk.Checkbutton(main_frame, text="Juice")
    juice_checkbutton.grid(row=9, column=0, sticky="W")

    coffee_checkbutton = ttk.Checkbutton(main_frame, text="Coffee")
    coffee_checkbutton.grid(row=10, column=1, sticky="W")

    order_button = ttk.Button(main_frame, text="Order")
    order_button.grid(row=10, columnspan=2)
    root.mainloop()


main()