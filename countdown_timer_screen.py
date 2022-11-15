from pathlib import Path
import tkinter as tk
import time
from tkinter import *
from tokenize import Double

from PIL import ImageTk, Image

#This creates the main window of an application
def countdown_timer_screen():
    window = Tk()
    window.title("Join")
    window.geometry("1280x720")
    window.configure(background='grey')

    #Number of seconds for countdown
    countdown_seconds = 1

    #Configure the background
    window.config(bg='black')

    #Create widgets for timer
    seconds = StringVar()
    Label(window, textvariable=seconds, width = 2, font = 'Helvetica 50', bg='black', fg="red").place(x=600, y=300)
    seconds.set(countdown_seconds)
    
    while countdown_seconds > -1 and window.winfo_exists():
        #Update the time
        window.update()
        time.sleep(1)
        countdown_seconds -= 1
        seconds.set(countdown_seconds)

    if countdown_seconds < 0:
        window.destroy()
    window.mainloop()

if __name__ == '__main__':
    countdown_timer_screen()
