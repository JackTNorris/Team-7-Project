from tkinter import *
from tkinter.tix import COLUMN
import tkinter.messagebox as toast

window = Tk()
player_entry_width = 15
frame_border_width = 40
def callback():
    print("pressed")

def generate_player_entries():

    frameRed = Frame(width=200, height=200,padx=frame_border_width,pady=frame_border_width, bg="red")

    frameGreen = Frame(width=100, height=100,padx=frame_border_width,pady=frame_border_width, bg="green")

    frameRed.grid(row=0, column=0, sticky="e")
    frameGreen.grid(row=0, column=1, sticky="w")

    frameRed.config(bg="red")
    frameGreen.config(bg="green")

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
            red_player_input_col.append(Entry(frameRed, width=player_entry_width))
            green_player_input_col.append(Entry(frameGreen, width=player_entry_width))
            red_player_input_col[j].grid(row = j, column = i)
            green_player_input_col[j].grid(row = j, column = i)
        red_player_inputs.append(red_player_input_col)
        green_player_inputs.append(green_player_input_col)
    red_player_inputs[0][0].focus_set()
    return red_player_inputs, green_player_inputs


def player_input_screen():
    WIN_WIDTH = 1280
    WIN_HEIGHT = 720
    window.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')

    red_player_inputs, green_player_inputs = generate_player_entries()

    def on_focus_out(event):
        for i in range(2):
            for j in range(15):
                if event.widget == red_player_inputs[i][j]:
                    if  i == 0: # checking to see if a first column input
                        entry_widget = event.widget
                        if entry_widget.get().isnumeric():
                            print("AWESOME")
                        else:
                            toast.showinfo("Invalid Input", "Enter in a number")
                            entry_widget.delete(0, END)


    window.bind('<FocusOut>', on_focus_out)

    window.mainloop()

    entry= Entry(window, width= 40)

if __name__ == '__main__':
    player_input_screen()
