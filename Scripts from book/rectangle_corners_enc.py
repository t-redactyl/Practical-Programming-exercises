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