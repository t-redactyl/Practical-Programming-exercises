class Arthropod(Organism):
    '''An arthropod that has a fixed number of legs.'''
    
    def __init__(self, name, x, y, legs):
        '''An arthropod with the given number of legs that exists at location
        (x, y) in the tide pool.'''
        
        Organism.__init__(self, name, x, y) 
        # We call the constructor from class Organism        
        self.legs = legs