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

    path = "Aaron.jpg"
    # window.state('zoomed')
    width =   1280 #int(window.winfo_width()) #
    height =  720 #int(window.winfo_height()) #

    #Configure the background
    window.config(bg='burlywood1')
    #Create Entry Widgets for SS
    seconds = StringVar()
    Entry(window, textvariable=seconds, width = 2, font = 'Helvetica 14').place(x=220, y=120)
    seconds.set('30')

    #Start the GUI
    
    times = 30
    while times > -1:
        #Update the time
        window.update()
        time.sleep(1)
        times -= 1
        seconds.set(times)

    Label(window, font =('Helvetica bold',22), text = 'Set the Timer',bg ='burlywood1').place(x=105,y=70)
    Button(window, text='START', bd ='2', bg = 'IndianRed1',font =('Helveticabold',10), command = countdowntimer).place(x=167, y=165)
    window.mainloop()

if __name__ == '__main__':
    countdown_timer_screen()
