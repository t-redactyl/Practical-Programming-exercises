def read_all_molecules(r):
    '''Read zero or more molecules from reader r, returning a list of the
    molecules read.
    
    Note that function read_molecule() is not defined in this function.'''
    
    result = []
    read = True
    while reading:
        molecule = read_molecule(r)
        if molecule:
            result.append(molecule)
        else:
            reading = False
    return result

