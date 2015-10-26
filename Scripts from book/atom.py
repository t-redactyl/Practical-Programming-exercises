class Atom(object):
    '''An atom with a number, symbol and coordinates.'''
    
    def __init__(self, num, sym, x, y, z):
        '''Create an Atom with number num, string symbol sym, and float
        coordinates (x, y, z).'''
        
        self.number = num
        self.center = (x, y, z)
        self.symbol = sym
        
    def __str__(self):
        '''Return a string representation of this Atom in this format:
        
        (SYMBOL, X, Y, Z)
        '''
        
        return '(%s, %s, %s, %s)' % \
               (self.symbol, self.center[0], self.center[1], self.center[2])
    
    def __repr__(self):
        '''Return a string representation of this Atom in this format:
        
        Atom("SYMBOL", X, Y, Z)
        '''
        
        return 'Atom(%s, "%s", %s, %s, %s)' % \
               (self.number, self.symbol, \
                self.center[0], self.center[1], self.center[2])
    
    def translate(self, x, y, z):
        '''Move this atom by adding (x, y, z) to its coordinates.'''
        
        self.center = (self.center[0] + x,
                       self.center[1] + y,
                       self.center[2] + z)