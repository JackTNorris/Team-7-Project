import queue
from tkinter import Tk
from screens.player_input_screen import player_input_screen
from splash_screen import splash_screen
from countdown_timer_screen import countdown_timer_screen
from player_action_screen import player_action_screen
from udp_thread import create_thread

#this will be the entry point of our application

#run splash screen

splash_screen()
players = player_input_screen()
countdown_timer_screen()

q = queue.Queue()
create_thread(q)
player_action_screen(players)
#tempororary for hector and gideon

print(players)

# main
# C:/Users/mitch/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/mitch/Documents/College/Fall 2022/Software Engineering/Project/Team-7-Project/main.py"
# server
# C:/Users/mitch/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/mitch/Documents/College/Fall 2022/Software Engineering/Project/Team-7-Project/misc/udp_serv.py"
# client
# C:/Users/mitch/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/mitch/Documents/College/Fall 2022/Software Engineering/Project/Team-7-Project/misc/udp_cli.py"
# # traffic test
# C:/Users/mitch/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/mitch/Documents/College/Fall 2022/Software Engineering/Project/Team-7-Project/misc/udp_traffictest.py"
