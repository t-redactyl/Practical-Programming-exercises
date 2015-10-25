from merge import merge

def mergesort(L):
    '''Sort L in increasing order.'''
    
    # Make a list og 1-item lists sp that we can start merging.
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])
        
    # The next two lists to merge are workspace[i] and workspace[i + 1].
    i = 0
    
    # As long as there are at least two more lists to merge, merge them.
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L2, L2)
        workspace.append(newL)
        i += 2
        
    # Copy the result back inot L
    if len(workspace) != 0:
        L[:] = workspace[-1][:]