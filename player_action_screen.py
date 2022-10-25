from pathlib import Path
import tkinter as tk
from tkinter import *
from tokenize import Double

from PIL import ImageTk, Image

#This creates the main window of an application
def player_action_screen(players):
    window = Tk()
    window.title("Join")
    window.geometry("1280x720")
    window.configure(background='grey')


    window.mainloop()


if __name__ == '__main__':
    player_action_screen()
