from tkinter import *
from tkinter.tix import COLUMN

window = Tk()
player_entry_width = 15
def callback():
    print("pressed")

def generate_player_entries():
    frame1 = Frame(window)
    frame2 = Frame(window)

    frame1.grid(row=0, column=0, sticky="nsew")
    frame2.grid(row=0, column=1, sticky="nsew")

    window.grid_columnconfigure(0, weight=1, uniform="group1")
    window.grid_columnconfigure(1, weight=1, uniform="group1")
    window.grid_rowconfigure(0, weight=1)

    red_player_inputs = []
    green_player_inputs = []
    for i in range(2):
        red_player_input_col = []
        green_player_input_col = []
        for j in range(15):
            print()
            red_player_input_col.append(Entry(frame1, width=player_entry_width))
            green_player_input_col.append(Entry(frame2, width=player_entry_width))
            red_player_input_col[j].grid(row = j, column = i)
            green_player_input_col[j].grid(row = j, column = i)
        red_player_inputs.append(red_player_input_col)
        green_player_inputs.append(green_player_input_col)

    return red_player_inputs, green_player_inputs

def player_input_screen():
    WIN_WIDTH = 1100
    WIN_HEIGHT = 750
    window.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')

    generate_player_entries()
    window.mainloop()

    entry= Entry(window, width= 40)

if __name__ == '__main__':
    player_input_screen()