# Practical Programming Chapter 14 notes

# Tkinter is the in-built Python module for creating GUIs. Every Tkinter
# GUI application starts by creating a 'root window' and saving a reference
# to it in a variable.

from Tkinter import *

window = Tk()

# The root window is initially empty. We develop the GUI by adding widgets to
# the root window.

# Labels display short pieces of text. We need to specify the parent widget
# (window) when we create a label.
label = Label(window, text="This is our label.")

# We also need to specify the 'pack' method, which tells label (and other widgets)
# to place itself in the parent and resize as necessary.
label.pack()

# Label is used to display static text, but can be used to display changing text
# too.

# Mutable variables
# Tkinter provides types that can be updated in place and can notify widgets
# whenever their values change. The values are set and retrieved using the set
# and get methods.

from Tkinter import *
window = Tk()
data = StringVar()
data.set("Data to display") # Any time this is changed, the label will change
label = Label(window, textvariable=data)
label.pack()
window.mainloop()

# Note that you cannot create mutable variables until the Tk() window has been
# called.

# Frames are widgets that organise other widgets.
from Tkinter import *

window = Tk()
frame = Frame(window)
frame.pack()
first = Label(frame, text="First label")
first.pack()
second = Label(frame, text="Second label")
second.pack()
third = Label(frame, text="Third label")
third.pack()

# Multiple frames can be used for finer formatting
from Tkinter import *

window = Tk()
frame = Frame(window)
frame.pack()
frame2 = Frame(window, borderwidth=4, relief=GROOVE)
frame2.pack()
first = Label(frame, text="First label")
first.pack()
second = Label(frame2, text="Second label")
second.pack()
third = Label(frame2, text="Third label")
third.pack()

# User input
# Two widgets allow users to enter text. The first is Entry, which allows
# a single line of text, and if StringVar is associated with it, then when
# the user types anything into entry, the StringVar's value will automatically
# be updated to the contents of the Entry.

from Tkinter import *

window = Tk()

frame = Frame(window)
frame.pack()
var = StringVar()
label = Label(frame, textvariable=var)
label.pack()
entry = Entry(frame, textvariable=var)
entry.pack()

window.mainloop()

# A view is something that displays information to the user, like Label.
# Views (like Entry) can also take user input, but they can't do anything
# else like calculations, etc.

# A model just stores data and keeps track of the applications current state.

# A controller carry out the actions in an application.

# Using Lambda
# These are one-line functions that are not named, e.g., this:
def f():
    return 3
f()

# can be represented as this:
(lambda: 3)()

# Lambdas can also take arguments:
(lambda x: 2 * x)(3)

# Lambdas do not store any variables, or change existing ones.

# Style
# Font

from Tkinter import *
window = Tk()
button = Button(window, text="Hello", font=("Courier", 14, "bold italic"))
button.pack()
window.mainloop

# Colors

from Tkinter import *
window = Tk()
button = Label(window, text="Hello", bg="green", fg="white")
button.pack()
window.mainloop()

# Layout

from Tkinter import *
window = Tk()
frame = Frame(window)
frame.pack()
label = Label(frame, text="Name")
label.pack(side="left")
entry = Entry(frame)
entry.pack(side="left")
window.mainloop()

# Grid layout

from Tkinter import *
window = Tk()
frame = Frame(window)
frame.pack()
label = Label(frame, text="Name:")
label.grid(row=0, column=0)
entry = Entry(frame)
entry.grid(row=1, column=1)
window.mainloop()

# A few more commonly used widgets
# Text - allows for multiple lines of text entry (versus Entry).

from Tkinter import *

def cross(text):
    text.insert(INSERT, 'X')

window = Tk()
frame = Frame(window)
frame.pack()

text = Text(frame, height=3, width=10)
text.pack()

button = Button(frame, text="Add", command=lambda: cross(text))
button.pack()

window.mainloop()

# Checkbuttons

from Tkinter import *

window = Tk()
frame = Frame(window)
frame.pack()
red = IntVar()
green = IntVar()
blue = IntVar()

for (name, var) in (('R', red), ('G', green), ('B', blue)):
    check = Checkbutton(frame, text=name, variable=var)
    check.pack(side='left')
def recolor(widget, r, g, b):
    color = '#'
    for var in (r, g, b):
        color += 'FF' if var.get() else '00'
    widget.config(bg=color)
	
label = Label(frame, text='[       ]')
button = Button(frame, text='update',
                command=lambda: recolor(label, red, green, blue))
button.pack(side='left')
label.pack(side='left')
window.mainloop()

# Menu

from Tkinter import *
import tkFileDialog as dialog

def save(root, text):
  data = text.get('0.0', END)
  filename = dialog.asksaveasfilename(
      parent=root,
      filetypes=[('Text', '*.txt')],
      title='Save as...')
  writer = open(filename, 'w')
  writer.write(data)
  writer.close()

def quit(root):
  root.destroy()
  
window = Tk()
text = Text(window)
text.pack()

menubar = Menu(window)
filemenu = Menu(menubar)
filemenu.add_command(label='Save', command=lambda : save(window, text))
filemenu.add_command(label='Quit', command=lambda : quit(window))

menubar.add_cascade(label = 'File', menu=filemenu)
window.config(menu=menubar)

window.mainloop()

# GUIs have bettern structure when they are object-orientated