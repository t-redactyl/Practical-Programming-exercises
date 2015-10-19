# Chapter 5 notes
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
print whales[0]
print whales[1]
print whales[12]
print whales[13]

print whales[-1]
print whales[-2]
print whales[-14]

third = whales[2]
print 'Third day:', third

# Lists can contain data of all classes
krypton = ['Krypton', 'Kr', -157.2, -153.4]
print krypton[1]
print krypton[2]

# Modifying lists
nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']
nobles[1] = 'neon' # Replace 'none' with 'neon'

# Built in functions on lists
half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
print "The length of the list 'half_lives' is %d" % len(half_lives)
print "The maximum of the list 'half_lives' is %f" % max(half_lives)
print "The minimum of the list 'half_lives' is %f" % min(half_lives)
print "The sum of the list 'half_lives' is %f" % sum(half_lives)

i = 2
i < len(half_lives)
half_lives[i]

j = 5
j < len(half_lives)

# List concatenation
original = ['H', 'He', 'Li']
final = original + ['Be']
final

# Multiplying lists
metals = 'Fe Ni'.split() # Create the list by splitting a string
metals * 3

# For loops and lists
velocities = [0.0, 9.81, 19.62, 29.43]
for v in velocities:
    print "Metric:", v, "m/sec;",
    print "Imperial:", v * 3.28, "ft/sec"

# Nested loops
outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']
for metal in outer:
    for halogen in inner:
        print metal + halogen

# Slicing
celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
useful_markers = celegans_markers[0:4] # Note that the new list doesn't include 4

# Aliasing
celegans_markers = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
celegans_copy = celegans_markers 
# This is distinct from saying celegans_copy = celegans_markers[:]
celegans_markers[5] = 'Lvl'
print celegans_markers
print celegans_copy

def sort_and_reverse(L):
    '''Return list L sorted and reversed.'''
    L.sort()
    L.reverse()
    return L

# List methods
colors = 'red orange green black blue'.split()
colors.append('purple')
colors
colors.insert(2, 'yellow')
colors.remove('black')

# Nested lists
life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
life[0]
life[0][1]
canada = life[0]
canada[0]

# Other kinds of sequences
# Strings are sequences (an immutable sequence of characters)

rock = 'anthracite'
rock[9]
rock[0:3]
rock[-5:]

# Tuples
# Tuples are like an immutable list
bases = ('A', 'C', 'G', 'T')
for b in bases:
    print b

life = (['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0])
life[0]

# Tuples cannot be changed once created, but objects inside can be changed
life[0][1] = 80.0

# Files as lists
file = open("/Users/jburchell/Documents/Python tutorials/Mary had a little lamb.txt", "r")
data = open("/Users/jburchell/Documents/Python tutorials/data.txt", "r")
for line in data:
    print len(line)

data = open('data.txt', 'r')
for line in data:
    print(len(line.strip())