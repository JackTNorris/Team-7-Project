from pathlib import Path
import tkinter as tk
from tkinter import *
from tokenize import Double
from tkinter.font import Font

from PIL import ImageTk, Image

player_border_width = 10
frame_border_width = 20

#This creates the main window of an application
def player_action_screen(players):
    window = Tk()
    window.title("Join")
    window.geometry("1280x720")
    window.configure(background='grey')

    helveticaBig = Font(family='Helvetica', size=20, weight='bold')
    helveticaSmall = Font(family='Helvetica', size=10, weight='bold')
    
    window.configure(bg = "black")

    
    frameRed = Frame(width=300, height=300,padx=frame_border_width,pady=frame_border_width, bg="black")
    frameGreen = Frame(width=300, height=300,padx=frame_border_width,pady=frame_border_width, bg="black")
    frameTimer = Frame(width=300, height=300,padx=frame_border_width,pady=frame_border_width, bg="black")
    frameEventBoxLeft = Frame(width=300, height=300,padx=frame_border_width,pady=frame_border_width, bg="white")
    frameEventBoxCenter = Frame(width=300, height=300,padx=frame_border_width,pady=frame_border_width, bg="white")
    frameEventBoxRight = Frame(width=300, height=300,padx=frame_border_width,pady=frame_border_width, bg="white")

    frameRed.grid(row=0, column=0, sticky="nsew")
    frameGreen.grid(row=0, column=2, sticky="nsew")
    frameTimer.grid(row=0, column=1, sticky="nsew")
    frameEventBoxLeft.grid(row=1, column=0, sticky="nsew")
    frameEventBoxCenter.grid(row=1, column=1, sticky="nsew")
    frameEventBoxRight.grid(row=1, column=2, sticky="nsew")
    
    frameRed.config(bg="grey")
    frameGreen.config(bg="grey")

    Label(frameRed, text="RED TEAM", bg="black", font=helveticaBig, fg="red").grid(row=0, column=0, sticky="e")
    Label(frameGreen, text="GREEN TEAM", bg="black", font=helveticaBig, fg="green").grid(row=0, column=0, sticky="w")
    Label(frameTimer, text="INSERT TIMER HERE", bg="grey", font=helveticaBig, fg="white").grid(row=0, column=1, sticky="n")
    Label(frameEventBoxCenter, text="EVENT WINDOW", bg="white", font=helveticaBig, fg="black").grid(row=0, column=1, sticky="n")


    window.grid_columnconfigure(0, weight=1, uniform="group1")
    window.grid_columnconfigure(1, weight=1, uniform="group1")
    window.grid_columnconfigure(2, weight=1, uniform="group1")
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)

    #'''
    for team in players:
        print('>Team: ', team)

        redRowNum = 1
        greenRowNum = 1
        redColNum = 0
        greenColNum = 0

        for player in players[team]:
            playerName = player['codename']
            
            if team == 'red_users':    
                # prevent overfill and go ovr to new column
                if redRowNum == 8:
                    redColNum += 1
                    redRowNum = 1

                Label(frameRed, text=playerName, fg="red", font=helveticaSmall, padx=player_border_width, pady=player_border_width, bg="black").grid(row=redRowNum, column=redColNum, sticky="w")
                redRowNum += 1
            else:
                # prevent overfill and go ovr to new column
                if greenRowNum == 8:
                    greenColNum += 1
                    greenRowNum = 1

                Label(frameGreen, text=playerName, fg="green", font=helveticaSmall, padx=player_border_width, pady=player_border_width,  bg="black").grid(row=greenRowNum, column=greenColNum, sticky="w")
                greenRowNum += 1

            print('   >player: ', playerName)
            
    #'''



    window.mainloop()

if __name__ == '__main__':
    player_action_screen()
