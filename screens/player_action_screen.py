import time
import tkinter as tk
from pathlib import Path
from tkinter import *
from tokenize import Double
from tkinter.font import Font
from PIL import ImageTk, Image
import threading


player_border_width = 10
frame_border_width = 20
warning_timer_seconds = 6 * 60

#This creates the main window of an application
def player_action_screen(players, event_queue):
    global warning_timer_seconds
    window = Tk()
    window.title("Join")
    window.geometry("1280x720")
    window.configure(background='grey')

    helveticaBig = Font(family='Helvetica', size=20, weight='bold')
    helveticaSmall = Font(family='Helvetica', size=10, weight='bold')
    
    window.configure(bg = "black")

    player_frame_heights = 720 / 2
    player_frame_widths = 1280 / 3
    
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
            
    seconds = StringVar()
    Label(frameTimer, textvariable=seconds, bg="black", font="Helvetica 50", fg="white").grid(row=0, column=1, sticky="n")
    seconds.set(get_minute_second_string(warning_timer_seconds))

    # seperate thread for timer. updating seconds widget triggers event to update window
    timer_thread = threading.Thread(target=increment_timer, args=(seconds,))
    timer_thread.start()

    def add_events_to_window(event_string):
        print("put code here for adding events to window")

    def listen_for_events(q):
        while True:
            #splitting "4:1" into "[4, 1]"
            event_data = q.get().split(":")

            #getting array of all players to search through
            all_players = players["red_users"] + players["green_users"]

            #filtering all_players for items with selected id, then selecting codename   
            codename_one = list(filter(lambda player: str(player["id"]) == event_data[0], all_players))[0]["codename"]
            codename_two = list(filter(lambda player: str(player["id"]) == event_data[1], all_players))[0]["codename"]

            event_string = codename_one + " hit " + codename_two

            #TODO: Remove this when you're adding the events to the screen
            print(event_string)

            add_events_to_window(event_string)
            q.task_done()

    event_listener_thread = threading.Thread(target=listen_for_events, args=(event_queue,))
    event_listener_thread.start()
    # close the window after the timer has expired
    window.after((warning_timer_seconds + 1) * 1000, window.destroy)
    
    window.mainloop()

    timer_thread.join()
    event_listener_thread.join()

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

def increment_timer(seconds):
    global warning_timer_seconds
    while warning_timer_seconds > -1:
        time.sleep(1)
        warning_timer_seconds -= 1
        if warning_timer_seconds > -1:
            seconds.set(get_minute_second_string(warning_timer_seconds))

if __name__ == '__main__':
    player_action_screen()