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