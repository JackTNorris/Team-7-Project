from pathlib import Path
import tkinter as tk
from tkinter import *
from tokenize import Double

from PIL import ImageTk, Image

#This creates the main window of an application
def countdown_timer_screen():
    window = Tk()
    window.title("Join")
    window.geometry("1280x720")
    window.configure(background='grey')

    path = "Aaron.jpg"
    # window.state('zoomed')
    width =   1280 #int(window.winfo_width()) #
    height =  720 #int(window.winfo_height()) #

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open("splash_screen.jpeg").resize((width, height)))
    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = tk.Label(window, image = img)

    #The Pack geometry manager packs widgets in rows or columns.
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    #Start the GUI
    window.after(3000, window.destroy)

    window.mainloop()


if __name__ == '__main__':
    countdown_timer_screen()
