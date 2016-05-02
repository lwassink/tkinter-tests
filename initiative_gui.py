from tkinter import *
from tkinter import ttk

# allow metawidgits like scrollable frames
import Pmw

# setup root window
root = Pmw.initialise()
root.title("Initiative tracker")

# highest level frame. It will contain all the other stuff
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

# button to add a new character
ttk.Button(mainframe, text="New").grid(column=1, row=1)

# scrollable frame to hold the characters
charframe = Pmw.ScrolledFrame(mainframe)
charframe._clipper.config(width=400, height=600)
charframe.interior().configure(bg='yellow')
charframe.grid(column=1, row=2)

# frame for character 1
test_label = ttk.Label(charframe.interior(), text="test")
test_label.grid(column=1, row=1)

# initiative for character 1
#ttk.Label(char1, text="Initiative").grid(column=1, row=1)

# put space around widgits
for child in mainframe.winfo_children():
     child.grid_configure(padx=5, pady=5)

# run things
root.mainloop()
