# Practical Programming Chapter 9 notes

# Sets are an unordered collection of distinct items
# Equivalent to the mathematical concept

# Empty set
set()

# The set function must be passed a single collection
set((2, 3, 5))
set([1, 2, 3])
set("abc")

# Sets do not have repeating elements
set((1, 2, 2, 3))
set("carrots")

# Set operations
ten = set(range(10))
lows = set([0, 1, 2, 3, 4])
odds = set([1, 3, 5, 7, 9])
lows.add(9)
lows
lows.difference(odds)
lows.intersection(odds)
lows.issubset(ten)
lows.issuperset(odds)
lows.remove(0)
lows
lows.symmetric_difference(odds)
lows.union(odds)
lows.clear()
lows

# Sets are stored in a hash table. Everytime an item is added to a set, 
# Python calculates a hash code for the item which is an integer that is
# guaranteed to the same for items with equal values.
hash('123')

# Hash codes can only be assigned to immutable objects (Booleans, numbers,
# strings and tuples, but not lists)
hash((1, 2, 3))
hash([1, 2, 3])

# Sets are also mutable, so we cannot normally have a set of sets. As such.
# Python has a concept called a 'frozen set' (a set whose contents cannot be
# changed).
frozenset()
frozenset((1, 2, 3))

# Dictionaries
# Associate a value with a key (like a phone book associates a phone number
# with a name).
# Keys form a set
birds = {'canada goose' : 3, 'northern fulmar' : 1}
# Dictionaries are indexed with keys, which returns the value
birds['northern fulmar']
birds['canada goose']

# Testing if a key is in a dictionary:
birds = {'eagle' : 999, 'snow goose' : 33}
if 'eagle' in birds:
    print 'eagles have been seen'
else:
    print 'no eagles here!'
    
del birds['eagle']
if 'eagle' in birds:
    print 'eagles have been seen'
else:
    print 'no eagles here!'
    
# Updating and membership
birds = {}
birds['snow goose'] = 33
birds['eagle'] = 999 # Wrong number!
birds
birds['eagle'] = 9
birds

# Removing entries
del birds['snow goose']

# Loops take the form of 'for key in dictionary'
birds = {'canada goose' : 183, 'long-tailed jaegar' : 71,
         'snow goose' : 63, 'northern fulmar' : 1}
for x in birds:
    print x, birds[x]