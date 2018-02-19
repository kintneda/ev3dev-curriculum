"""This is the place to test the image insertion for the final project."""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
img = ImageTk.PhotoImage(Image.open("clingmans_dome1.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
