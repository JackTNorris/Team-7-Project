from tkinter import Tk
from screens.player_input_screen import player_input_screen
from splash_screen import splash_screen
from countdown_timer_screen import countdown_timer_screen
from player_action_screen import player_action_screen

#this will be the entry point of our application


#run splash screen

splash_screen()
players = player_input_screen()
countdown_timer_screen()

player_action_screen(players)
#tempororary for hector and gideon


print(players)
