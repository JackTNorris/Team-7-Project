from queue import Queue
from screens.player_input_screen import player_input_screen
from screens.splash_screen import splash_screen
from screens.countdown_timer_screen import countdown_timer_screen
from screens.player_action_screen import player_action_screen
from services.udp_serv import run_udp_thread, start_server


# This will be the entry point of our application

# Run splash screen
splash_screen()
players = player_input_screen()
countdown_timer_screen()

# Create queue to hold events
q = Queue()

# Start UDP server and thread to fetch traffic
sock = start_server()
run_udp_thread(q, sock)

player_action_screen(players, q)
