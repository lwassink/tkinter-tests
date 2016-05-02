from tkinter import *
from tkinter import ttk

# function to convert feet to meters
def calculate(*args):
   try:
      value = float(feet.get())
      meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
   except ValueError:
      pass

root = Tk()
root.title("Feet to Meters")

# define frame to hold the other widgits
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, E, W, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# variables for number of feet and meters
feet = StringVar()
meters = StringVar()

# get feet from a text entry
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W,E)) #position the text entry

# display meters with a label
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))

# a button to run the calculation
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

#some other labels
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# add space around all the widgits
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# start with focus on text entry
feet_entry.focus()

# pressing the return key executes the calculate function
root.bind('<Return>', calculate)

# run things
root.mainloop()
