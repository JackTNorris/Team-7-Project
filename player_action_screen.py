from pathlib import Path
import tkinter as tk
from tkinter import *
from tokenize import Double
from tkinter.font import Font
import time
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

    player_frame_heights = 720 / 2
    player_frame_widths = 1280 / 3
    
    warning_timer_seconds = 60 * 6

    frameRed = Frame(width=player_frame_widths, height=player_frame_heights,padx=frame_border_width,pady=frame_border_width, bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
    frameGreen = Frame(width=player_frame_widths, height=player_frame_heights,padx=frame_border_width,pady=frame_border_width, bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
    frameTimer = Frame(width=player_frame_widths, height=player_frame_heights,padx=frame_border_width,pady=frame_border_width, bg="black", highlightbackground="blue", highlightcolor="blue", highlightthickness="2")
    frameEventBoxLeft = Frame(width=player_frame_widths, height=player_frame_heights,padx=frame_border_width,pady=frame_border_width, bg="black")
    frameEventBoxCenter = Frame(width=player_frame_widths, height=player_frame_heights,padx=frame_border_width,pady=frame_border_width, bg="black")
    frameEventBoxRight = Frame(width=player_frame_widths, height=player_frame_heights,padx=frame_border_width,pady=frame_border_width, bg="black")

    frameRed.grid(row=0, column=0, sticky="nsew")
    frameGreen.grid(row=0, column=2, sticky="nsew")
    frameTimer.grid(row=0, column=1, sticky="nsew")
    frameEventBoxLeft.grid(row=1, column=0, sticky="nsew")
    frameEventBoxCenter.grid(row=1, column=1, sticky="nsew")
    frameEventBoxRight.grid(row=1, column=2, sticky="nsew")
    
    # frameRed.config(bg="grey")
    # frameGreen.config(bg="grey")

    Label(frameRed, text="RED TEAM", bg="black", font=helveticaBig, fg="red").grid(row=0, column=0, sticky="e")
    Label(frameGreen, text="GREEN TEAM", bg="black", font=helveticaBig, fg="green").grid(row=0, column=0, sticky="w")
    Label(frameEventBoxCenter, text="EVENT WINDOW", bg="black", font=helveticaBig, fg="white").grid(row=0, column=1, sticky="n")


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

    seconds = StringVar()
    Label(frameTimer, textvariable=seconds, bg="black", font="Helvetica 50", fg="white").grid(row=0, column=1, sticky="n")
    seconds.set(get_minute_second_string(warning_timer_seconds))
    

    while warning_timer_seconds > -1 and window.winfo_exists():
        #Update the time
        window.update()
        time.sleep(1)
        warning_timer_seconds -= 1
        seconds.set(get_minute_second_string(warning_timer_seconds))

    if warning_timer_seconds < 0:
        window.destroy()
    window.mainloop()

    window.mainloop()

def get_minute_second_string(seconds):
    #default to 00
    seconds_text = "00" 
    minutes_text = "00"

    #if single digit second value
    if seconds % 60 < 10:
        seconds_text = "0" + str(seconds % 60)
    
    #if double digit second value
    elif seconds % 60 > 0:
        seconds_text = str(seconds % 60)


    #if single digit second value
    if seconds / 60 < 10:
        minutes_text = "0" + str(int(seconds / 60))
    
    #if double digit second value
    elif seconds / 60 > 0:
        minutes_text = str(int(seconds / 60))


    return  minutes_text + ":" + seconds_text

if __name__ == '__main__':
    player_action_screen()