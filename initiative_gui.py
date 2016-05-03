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
charframe._clipper.config(height=300)
charframe.grid(column=1, row=2)

# frame for character 1
char1 = ttk.Frame(charframe.interior())
char1.grid(column=1, row=1, sticky='new')
# initiative for character 1
ttk.Label(char1, text="Initiative").grid(column=1, row=1)
# initiative number
ttk.Label(char1, text="15").grid(column=2, row=1)
# NPC check box label
ttk.Label(char1, text="NPC:").grid(column=1, row=2, sticky='e')
# NPC check box
ttk.Checkbutton(char1).grid(column=2, row=2)
# delete button
ttk.Button(char1, text="Delete").grid(column=3, row=2)

# put space around widgits
for child in mainframe.winfo_children():
     child.grid_configure(padx=5, pady=5)

# run things
root.mainloop()
