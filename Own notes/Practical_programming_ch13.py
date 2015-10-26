# Practical Programming Chapter 13 notes

# Creating a simple color class:
class Color(object):
    '''An RGB color, with red, green and blue components.'''

# Assigning red, green and blue values (the bad way)
black.red = 0
black.green = 0
black.blue = 0

black.red
black.green
black.blue

# Objects are kind of like dictionaries, but more flexible. E.g.,
black = {"red" : 0, "green" : 0, "blue" : 0}

# Methods
# Below is a function that defines how light a color is:
def lightness(color):
    '''Return the lightness of color.'''
    strongest = max(color.red, color.green, color.blue)
    weakest = min(color.red, color.green, color.blue)
    return 0.5 * (strongest + weakest) / 255

# To make lightness a method of the class Color, we move the definition into
# the class.

class Color(object):
    '''An RGB color, with red, green and blue components.'''
    
    def lightness(self):
        '''Calculate the lightness of this color.'''
        
        strongest = max(self.red, self.green, self.blue)
        weakest = min(self.red, self.green, self.blue)
        return 0.5 * (strongest + weakest) / 255

# In addition, we replace the parameter color and replace it with 'self'. Python
# supplies the object by referring to the instance of the class.

purple = Color() 
# This is just like creating a list or other type, e.g, purple = "purple" or
# purple = ["P", "u", "r", "p", "l", "e"], a new instance of a string or a 
# list object is created.
purple.red = 255
purple.green = 0
purple.blue = 255
purple.lightness()

# If you do not assign variables to the parameter self, the method will fail:
'''This is an incorrect example of defining a method in a class.'''

class Color(object):
    '''An RGB color, with red, green and blue components.'''

    def lightness(self):
        '''Return the lightness of this color.'''
        
        #Fails: no such variables 'red', 'green', and 'blue'.
        strongest = max(red, green, blue)
        weakest = min(red, green, blue)
        return 0.5 * (strongest + weakest) / 255


# Constructors
# Assigning colors outside the variable is a bad idea, as it is inefficient
# and if you don't remember all of the right instance variables, it will fail.
# Instead, you construct the instance WITH PARAMETERS (similar to the way
# you call arguments in a function. This is called a constructor, and you 
# call it using __init__:

class Color(object):
    '''An RGB color, with red, green and blue components.'''
    
    def __init__(self, r, g, b):
        '''A new color with red value r, green value g, and blue value b. 
        All components are integers in the range 0-255.'''
        
        self.red = r
        self.green = g
        self.blue = b

# Double underscores around __init__ indicate that this method has a special
# meaning to Python - this is the method to be called when a new object is
# being created. Note that as with all object methods, the __init__ function
# has to pass an argument to the object itself (self). This indicates that
# a blank (color) object is to be created.

# Special methods make our types (classes) act like Pythons built-in types 
# (e.g., Bools). The two main methods are __str__ and __repr__. __str__ gives
# back a less precise but human readable version of the output, while __repr__
# gives a more precise but less readable version of the output.

# The __str__ method:

class Color(object):
    '''An RGB color, with red, green and blue components.'''
    
    def __init__(self, r, g, b):
        '''A new color with red value r, green value g, and blue value b. 
        All components are integers in the range 0-255.'''
        
        self.red = r
        self.green = g
        self.blue = b
    
    def __str__(self):
        '''Return a string representation of this Color in the form of an 
        RGB tuple.'''
        
        return '(%s, %s, %s)' % (self.red, self.green, self.blue)

purple = Color(128, 0, 128)
print purple

# Python has a bunch of other special methods, including: 
# __add__ - add objects with +
# __sub__ - subtract objects with -
# __eq__ - compare objects with ==

class Color(object):
    '''An RGB color, with red, green and blue components.'''
    
    def __init__(self, r, g, b):
        '''A new color with red value r, green value g, and blue value b.
        All components are integers in the range 0-255.'''
        
        self.red = r
        self.green = g
        self.blue = b
    
    def __str__(self):
        '''Return a string representation of this Color in the form 
        Color(red, green, blue).'''
        
        return 'Color(%s, %s, %s)' % (self.red, self.green, self.blue)
    
    def __add__(self, other_color):
        '''Return a new Color made from adding the red, green and blue 
        components of this Color to Color other_color's components. If
        the sum is greater than 255, then the color is set to 255.'''
        
        return Color(min(self.red + other_color.red, 255),
                     min(self.green + other_color.green, 255),
                     min(self.blue + other_color.blue, 255))
    
    def __sub__(self, other_color):
        '''Return a new Color made from subtracting the red, green and blue
        components of this Color from Color other_color's components. if
        the difference is less than 0, then the color is set to 0.'''
        
        return Color(max(self.red - other_color.red, 0),
                     max(self.green - other_color.green, 0),
                     max(self.blue - other_color.blue, 0))
    
    def __eq__(self, other_color):
        '''Return True is this Color's components are equal to Color other_color's
        components.'''
        
        return self.red == other_color.red and self.green == other_color.green \
               and self.blue == other_color.blue
    
    def lightness(self):
        '''Return the lightness of this color.'''
        
        #Fails: no such variables 'red', 'green', and 'blue'.
        strongest = max(red, green, blue)
        weakest = min(red, green, blue)
        return 0.5 * (strongest + weakest) / 255    

purple = Color(128, 0, 128)
white = Color(255, 255, 255)
dark_grey = Color(50, 50, 50)
print purple + dark_grey
print white - dark_grey
print white == Color(255, 255, 255)

# Use of methods must be done carefully. What if we used the __add__ method, but
# defined the + operator to modify the object it was being called on instead of
# creating a new one?

class Color(object):
    '''An RGB color, with red, green and blue components.'''
        
        def __init__(self, r, g, b):
            '''A new color with red value r, green value g, and blue value b.
            All components are integers in the range 0-255.'''
            
            self.red = r
            self.green = g
            self.blue = b
        
        def __str__(self):
            '''Return a string representation of this Color in the form 
            Color(red, green, blue).'''
            
            return 'Color(%s, %s, %s)' % (self.red, self.green, self.blue)
        
        def __add__(self, other_color):
            '''This is a bad way to define this method.'''    
            
            self.red += other_color.red
            self.green += other_color.green
            self.blue += other_color.blue
            return self
        
# While we can expand the functionality of operators using the special
# methods, it is very important that we do this in a way that is consistent
# with how these are used with the other Python types!

# More about dir and help
# The contents of our Color object include the instance variables and all the
# Color methods.

black = Color(0, 0, 0)
dir(black)

# We can get help as we have written docstrings:
help(Color)

# Towards the end of the help text, there is a __dict__ item, as Python 
# implements instance variables using dictionaries.

black.__dict__

# A little bit of OO theory
# Encapsulation
# The class hides the details of how a function/method is carried out, so that
# if changes are made to a class, the instances that call particular methods
# do not need to be rewritten.

class Rectangle(object):
    '''Represent a rectangular section of an image.'''
    
    def __init__(self, x0, y0, x1, y1):
        '''Create a rectangle with non-zero area. (x0, y0) is the lower left
        corner, (x1, y1) is the upper right corner.'''
        
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1    
        
    def area(self):
        '''Return the area of the rectangle.'''
        
        return (self.x1 - self.x0) * (self.y1 - self.y0)
    
    def contains(self, x, y):
        '''Return True if (x, y) point is inside a rectangle, and False 
        otherwise.'''
        
        return (self.x0 <= x <= self.x1) and \
               (self.y0 <= y <= self.y1)
    
R1 = Rectangle(1, 1, 2, 3) # Rectangle starting as (1, 1) and ending at (2, 3)
R1.area()
R1.contains(1, 2)

# What if I decided to change how rectangle was defined?

class Rectangle(object):
    '''Represent a rectangular section of an image.'''
    
    def __init__(self, x0, y0, width, height):
        '''Create a rectangle with non-zero area. (x0, y0) is the lower left
        corner, width and height are the X and Y extent.'''
        
        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height
    
    def area(self):
        '''Return the area of the rectangle.'''
        
        return self.width * self.height
    
    def contains(self, x, y):
        '''Return True if (x, y) point is inside a rectangle, and False 
        otherwise.'''
        
        return (self.x0 <= x) and (x <= self.x0 + width) and \
               (self.y0 <= y) and (y <= self.y0 + height)
    
# While we would obviously have the way rectangle instances are defined,
# the area and contains methods would not need to change.

# Polymorphism
# This means an expression involving a variable can do different things
# depending on the TYPE of the object to which the variable refers (i.e.,
# string versus list). E.g., operator '+' does different things depending
# on whether you are adding two strings or two integers.

# To make the rectangle class polymorphic (i.e., so someone can make their
# own rectangles), we need to properly encapsulate the class (i.e., so that
# the user does not have to manually calculate things like maximum X, this
# is instead done by a method written into the class). You can see in the 
# example below that I have now included methods for calculating the 
# minimum and maximum X and Y coordinates.

class Rectangle(object):
    '''Represent a rectangular section of an image.'''
    
    def __init__(self, x0, y0, x1, y1):
        '''Create a rectangle with non-zero area. (x0, y0) is the lower left
        corner, (x1, y1) is the upper right corner.'''
        
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1    
        
    def area(self):
        '''Return the area of the rectangle.'''
        
        return (self.x1 - self.x0) * (self.y1 - self.y0)
    
    def contains(self, x, y):
        '''Return True if (x, y) point is inside a rectangle, and False 
        otherwise.'''
        
        return (self.x0 <= x <= self.x1) and \
               (self.y0 <= y <= self.y1)
    
    def get_min_x(self):
        '''Return the minimum X coordinate.'''
        
        return self.x0
    
    def get_min_y(self):
        '''Return the minimum Y coordinate.'''
        
        return self.y0
    
    def get_max_x(self):
        '''Return the maximum X coordinate.'''
        
        return self.x1
    
    def get_max_y(self):
        '''Return the maximum Y coordinate.'''
        
        return self.y1

# Inheritance

class Organism(object):
    '''A thing that lives in a tide pool.'''
    
    def __init__(self, name, x, y):
        '''A living thing that is at location (x, y) in the tide pool.'''
        
        self.name = name
        self.x = x
        self.y = y
    
    def __str__(self):
        '''Return a string representation of this Organism.'''
        
        return '(%s, [%s, %s])' % (self.name, self.x, self.y)
    
    def can_eat(self, food):
        '''Report whether this Organism can eat the given food. Since we
        don't know anything about what a generic organism eats, this always
        returns False.'''
        
        return False
    
    def move(self):
        '''Ask the organism to move. By default, this does nothing, since we
        don't know anything about how fast or how far a generic organism would
        move.'''
        
        return
    
# We can now create a new Organism, an Arthropod:

class Arthropod(Organism):
    pass

# class Arthropod is a 'child' class which inherits the methods and instance
# variables from the 'parent' class organism:

blue_crab = Arthropod('Callinectes sapidus', 0, 0)
print blue_crab

# However, we want Arthopod to be more than just a generic Organism. As such, we
# give it its own instance variables, methods, or both. Below, we add a leg number
# constructor to Arthropod.

class Arthropod(Organism):
    '''An arthropod that has a fixed number of legs.'''
    
    def __init__(self, name, x, y, legs):
        '''An arthropod with the given number of legs that exists at location
        (x, y) in the tide pool.'''
        
        Organism.__init__(self, name, x, y) 
        # We call the constructor from class Organism        
        self.legs = legs
        
lobster = Arthropod('Homarus gammarus', 0, 0) # Will thrown an error
lobster = Arthropod('Homarus gammarus', 0, 0, 10) # Correct
print lobster

# Note that the result from organism (not including the number of legs) is
# printed. We need to override the __str__ method.

class Arthropod(Organism):
    '''An arthropod that has a fixed number of legs.'''
    
    def __init__(self, name, x, y, legs):
        '''An arthropod with the given number of legs that exists at location
        (x, y) in the tide pool.'''
        
        Organism.__init__(self, name, x, y)
        self.legs = legs
        
    def __str__(self):
        '''Return a string representation of this Arthropod.'''
        
        return '(%s, %s, [%s, %s])' % (self.name, self.legs, self.x, self.y)

# A child class can also have methods that are not part of the parent class.

class Arthropod(Organism):
    '''An arthropod that has a fixed number of legs.'''
    
    def __init__(self, name, x, y, legs):
        '''An arthropod with the given number of legs that exists at location
        (x, y) in the tide pool.'''
        
        Organism.__init__(self, name, x, y)
        self.legs = legs
    
    def __str__(self):
        '''Return a string representation of this Arthropod.'''
        
        return '(%s, %s, [%s, %s])' % (self.name, self.legs, self.x, self.y)
    
    def is_decapod(self):
        '''Return True is this Arthropod is a decapod.'''
        
        return self.legs == 10
    
    def leg_count(self):
        '''Return the number of legs this Arthropod possesses.'''
        
        return self.legs

lobster = Arthropod('Homarus gammarus', 0, 0, 10)
lobster.is_decapod()
lobster.leg_count()