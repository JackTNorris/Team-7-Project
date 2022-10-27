from tkinter import *
from tkinter.tix import COLUMN
import tkinter.messagebox as toast
import sys
from tkinter.font import Font
sys.path.append('../')
from services.database import user_exists, get_user, add_user

player_entry_width = 15
frame_border_width = 40

def player_input_screen():
    window = Tk()
    WIN_WIDTH = 1280
    WIN_HEIGHT = 720
    window.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
    window.resizable(False, False)
    helvetica20 = Font(family='Helvetica', size=20, weight='bold')
    head_label = Label(window, text="Edit Current Game",font=helvetica20, fg="white", bg="black")
    head_label.place(x=575, y=0)
    quit_label = Label(window, text="Press F5 to Quit.",font=helvetica20, fg="white", bg="black")
    quit_label.place(x=575, y=680)
    window.configure(bg = "black")
    red_users = []
    green_users = []

    def generate_player_entries():
        frameRed = Frame(width=200, height=200,padx=frame_border_width,pady=frame_border_width, bg="red")

        frameGreen = Frame(width=100, height=100,padx=frame_border_width,pady=frame_border_width, bg="green")

        
        frameRed.grid(row=0, column=0, sticky="e")
        frameGreen.grid(row=0, column=1, sticky="w")

        frameRed.config(bg="red")
        frameGreen.config(bg="green")
        Label(frameRed, text="Red Team", bg="red", fg="white").grid(row=0, column=0)
        Label(frameGreen, text="Green Team", bg="green", fg="white").grid(row = 0, column=0)
        window.grid_columnconfigure(0, weight=1, uniform="group1")
        window.grid_columnconfigure(1, weight=1, uniform="group1")
        window.grid_rowconfigure(0, weight=1)

        

        red_player_inputs = []
        green_player_inputs = []
        for i in range(1, 3):
            red_player_input_col = []
            green_player_input_col = []
            for j in range(1, 16):
                red_player_input_col.append(Entry(frameRed, width=player_entry_width))
                green_player_input_col.append(Entry(frameGreen, width=player_entry_width))
                red_player_input_col[j-1].grid(row = j, column = i)
                green_player_input_col[j-1].grid(row = j, column = i)
                Label(frameRed, text=j, bg="red").grid(row=j, column=0)
                Label(frameGreen, text=j, bg="green").grid(row = j, column=0)
            red_player_inputs.append(red_player_input_col)
            green_player_inputs.append(green_player_input_col)
        red_player_inputs[0][0].focus_set()
        return red_player_inputs, green_player_inputs 
    
    red_player_inputs, green_player_inputs = generate_player_entries()

    def next_id_entry(current):
        for i in range(2):
            for j in range(14):
                if red_player_inputs[i][j] == current:
                    return red_player_inputs[i][j+1]
                if green_player_inputs[i][j] == current:
                    return green_player_inputs[i][j+1]
        return NONE

    def next_codename_entry(current):
        for i in range(1):
            for j in range(15):
                if red_player_inputs[i][j] == current:
                    return red_player_inputs[i+1][j]
                if green_player_inputs[i][j] == current:
                    return green_player_inputs[i+1][j]
        return NONE

    # returns the corresponding id entry linked to a codename entry
    def corresponding_id_entry(codename_entry):
        for j in range(15):
            if red_player_inputs[1][j] == codename_entry:
                return red_player_inputs[0][j]
            if green_player_inputs[1][j] == codename_entry:
                return green_player_inputs[0][j]
        return NONE
    
    def on_focus_out(event):
        entry_widget = event.widget
        for i in range(2):
            for j in range(15):
                if entry_widget == red_player_inputs[i][j] or entry_widget == green_player_inputs[i][j]:
                    if  i == 0: # checking to see if a first column input
                        player_id = entry_widget.get()
                        if player_id.isnumeric():
                            codename_entry = next_codename_entry(entry_widget)
                            nxt_id_entry = next_id_entry(entry_widget)
                            if user_exists(entry_widget.get()):
                                codename = get_user(player_id)
                                if entry_widget == red_player_inputs[i][j]:
                                    red_users.append({"id": player_id, "codename": codename})
                                if entry_widget == green_player_inputs[i][j]:
                                    green_users.append({"id": player_id, "codename": codename})
                                codename_entry.delete(0, END)
                                codename_entry.insert(0, codename)
                                if nxt_id_entry != NONE:
                                    nxt_id_entry.focus_set()
                            else:
                                codename_entry.focus_set()
                        else:
                            if player_id != "":
                                toast.showinfo("Invalid Input", "Enter in a number")
                                entry_widget.delete(0, END)
                    if i == 1:
                        corr_id_entry = corresponding_id_entry(entry_widget)
                        corr_id_entry_val = corr_id_entry.get()
                        if corr_id_entry_val == "" and entry_widget.get() != "":
                            toast.showinfo("Invalid Op", "Must enter in id before codename")
                            entry_widget.delete(0, END)
                        else:
                            add_user(corr_id_entry_val, entry_widget.get())
                            next_id_entry(corr_id_entry).focus_set()

    def close_window(e):
        window.destroy()

    window.bind('<FocusOut>', on_focus_out)

    window.bind('<F5>', lambda e: close_window(e))

    window.mainloop()

    return {
        "red_users": red_users,
        "green_users": green_users
    }


if __name__ == '__main__':
    player_input_screen()
