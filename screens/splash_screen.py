import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
def splash_screen():
    window = tk.Tk()
    window.title("Join")
    window.geometry("300x300")
    window.configure(background='grey')

    path = "Aaron.jpg"

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open("./splash_screen.jpeg"))

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = tk.Label(window, image = img)

    #The Pack geometry manager packs widgets in rows or columns.
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    #Start the GUI


    window.mainloop()


if __name__ == '__main__':
    splash_screen()
