import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()
    root.title("Burger Stand Menu")

    main_frame = ttk.Frame(root, padding=25)
    main_frame.grid()

    burger_label = ttk.Label(main_frame, text="Burgers", font=("Helvetica", 16))
    burger_label.grid(row=0, column=0)

    quarter_pounder_checkbox = ttk.Checkbutton(main_frame, text="Quarter Pounder", offvalue=0, onvalue=1)
    quarter_pounder_checkbox.grid(row=1, column=0)

    half_pounder_checkbox = ttk.Checkbutton(main_frame, text="1/2 Pounder")
    half_pounder_checkbox.grid(row=1, column=1)

    cheeseburger_checkbox = ttk.Checkbutton(main_frame, text="Cheeseburger")
    cheeseburger_checkbox.grid(row=1, column=2)

    double_cheeseburger_checkbox = ttk.Checkbutton(main_frame, text="Double Cheeseburger")
    double_cheeseburger_checkbox.grid(row=1, column=3)

    fries_label = ttk.Label(main_frame, text="Fries", font=("Helvetica", 16))
    fries_label.grid(row=2, column=0)

    small_fries_checkbutton = ttk.Checkbutton(main_frame, text="Small")
    small_fries_checkbutton.grid(row=3, column=0)

    medium_fries_checkbutton = ttk.Checkbutton(main_frame, text="Medium")
    medium_fries_checkbutton.grid(row=3, column=1)

    large_fries_checkbutton = ttk.Checkbutton(main_frame, text="Large")
    large_fries_checkbutton.grid(row=3, column=2)

    drinks_label = ttk.Label(main_frame, text="Drinks", font=("Helvetica", 16))
    drinks_label.grid(row=4, column=0)

    water_checkbutton = ttk.Checkbutton(main_frame, text="Water")
    water_checkbutton.grid(row=5, column=0)

    soda_checkbutton = ttk.Checkbutton(main_frame, text="Soda")
    soda_checkbutton.grid(row=5, column=1)

    juice_checkbutton = ttk.Checkbutton(main_frame, text="Juice")
    juice_checkbutton.grid(row=5, column=2)
    
    coffee_checkbutton = ttk.Checkbutton(main_frame, text="Coffee")
    coffee_checkbutton.grid(row=5, column=3)
    root.mainloop()


main()