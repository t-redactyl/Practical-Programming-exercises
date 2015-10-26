'''Displays a GUI with a mutable value for 'label'. Any time the program changes the 
contents of 'data', the text the label is displaying will automatically 
change as well.'''

from Tkinter import *
window = Tk()
data = StringVar()
data.set("Data to display") # Any time this is changed, the label will change
label = Label(window, textvariable=data)
label.pack()
window.mainloop()