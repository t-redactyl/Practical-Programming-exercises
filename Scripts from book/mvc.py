'''A demonstration of models, views and controllers, where the model is a 
simple integer counter, the controller is the function click, and the view
is made up of 4 objects: the root window a frame, a Label that shows the 
current value of counter, and a button that the user can click to increment
counter's value.'''

# Initialisation
from Tkinter import *

# The controller
def click():
    counter.set(counter.get() + 1)

if __name__ == '__main__':
    # More initialisation
    window = Tk()
    
    # The model.
    counter = IntVar()
    counter.set(0)
    
    # The views.
    frame = Frame(window)
    frame.pack()
    button = Button(frame, text="Click", command=click) # Pass function click as command
    button.pack()
    
    label = Label(frame, textvariable=counter)
    label.pack()
    
    window.mainloop()