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
    
     def get_min_x(self):
        '''Return the minimum X coordinate.'''
        
        return self.x0
    
    def get_min_y(self):
        '''Return the minimum Y coordinate.'''
        
        return self.y0
    
    def get_max_x(self):
        '''Return the maximum X coordinate.'''
        
        return self.x0 + width
    
    def get_max_y(self):
        '''Return the maximum Y coordinate.'''
        
        return self.y0 + height