def find_two_smallest(L):
    '''Return a tuple of the indices of the two smallest values in list L.'''
    
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)
    next_smallest = min(L)
    min2 = L.index(next_smallest)
    
    return the two indices