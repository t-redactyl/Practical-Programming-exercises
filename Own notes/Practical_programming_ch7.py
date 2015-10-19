# Practical Programming Chapter 7

# Ranges of numbers
range(1, 5)
range(10)

sum = 0
for i in range(1, 4):
    sum += i

# Note that the answer is 6, not 10 (1 + 2 + 3), as the top number in the range is not included.

# Range can also increase by more than 1
range(2000, 2050, 4)
range(2050, 2000, -4)

values = ['a', 'b', 'c']
len(values)
range(3)
range(len(values))

for i in range(len(values)):
    print i
# This is obviously distinct from "for i in values".

for i in range(len(values)):
    print i, "\t", values[i]
    
# We can use this to overwrite list elements in a for loop

values = ['a', 'b', 'c']
for i in range(len(values)):
    values[i] = 'X'

# Let's use it to double each value in a list
values = [1, 2, 3]
for i in range(len(values)):
    values[i] = 2 * values[i]

# The enumerate function
# Takes a sequence (list, tuple or string) and returns a list of pairs containing
# the value and its index

for x in enumerate('abc'):
    print x

for x in enumerate(['Canada', 'United States', 'Mexico']):
    print x
    
for x in enumerate(('Cats', 'Dogs', 'Fish')):
    print x
    
# Using enumerate to double the values in a list
values = [1, 2, 3]
for pair in enumerate(values):
    i = pair[0]
    v = pair[1]
    values[i] = 2 * v

# Or...
values = [1, 2, 3]
for (i, v) in enumerate(values):
    values[i] = 2 * v
# Python allows multivalued assignment, which means that because enumerate
# produces 2 values (the index and the sequence value), you can assign two
# values on the left.

x, y = 1, 2

# Python will also 'explode' sequences on the right hand side
first, second, third = [1, 2, 3]

# Nested lists
# Ragged lists
info = [['Isaac Newton', 1643, 1727],
        ['Charles Darwin', 1809, 1882],
        ['Alan Turing', 1912, 1954, 'alan@bletchley.uk']]
for item in info:
    print len(item)

times = [["9:02", "10:17", "13:52", "18:23", "21:31"],
         ["8:45", "12:44", "14:52", "22:17"],
         ["8:55", "11:11", "12:34", "13:46", "15:52", "17:08", "21:15"],
         ["9:15", "11:44", "16:28"],
         ["10:01", "13:33", "16:45", "19:00"],
         ["9:34", "11:16", "15:52", "20:37"],
         ["9:01", "12:24", "18:51", "23:13"]]
for day in times:
    for time in day:
        print time,
    print

# While loops
rabbits = 3
while rabbits > 0:
    print rabbits
    rabbits -= 1

# The call stack
# Running functions are tracked using the a stack frame. Only the top frame in the stack is active, and the rest are paused until the functions above them are finished. Each stack gives a return address (where the call stack needs to go once the current function is finished) and a return value that is the product of the function call. Once Python works out where to next go, it removes that frame.

# User input loops
while True:
    formula = raw_input("Please enter a chemical formula: ")
    if formula == "H20":
        print "Water"
    elif formula == "NH3":
        print "Ammonia"
    elif formula == "CH3":
        print "Methane"
    else:
        print "Unknown compound"

# Controlling loops - break statements
current_line = 1
earth_line = 0
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    if line == "Earth":
        earth_line = current_line
    current_line = current_line + 1
print "Earth is at line %d" % earth_line

# Using a break statement
earth_line = 1
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    if line == "Earth":
        break
    earth_line = earth_line + 1
print "Earth is at line %d" % earth_line
# N.B. Break statements only exit the innermost loop, so in nested loops, the 
# outer loop will continue running.

# Controlling loops - continue statements
# Changed data.txt file so it is now commented...This program now gives the wrong answer
# because it counts the lines with the comments.
earth_line = 1
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    if line == "Earth":
        break
    earth_line = earth_line + 1
print "Earth is at line %d" % earth_line

# We can use the continue statement to get the correct answer.
entry_number = 1
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    if line.startswith("#"):
        continue
    if line == "Earth":
        break
    entry_number = entry_number + 1
print "Earth is the %dth-lightest planet." % entry_number

# An 'if' statement would also do the trick:
entry_number = 1
file = open("data.txt", "r")
for line in file:
    line = line.strip()
    if not line.startswith("#"):
        if line == "Earth":
            break
        entry_number = entry_number + 1
print "Earth is the %dth-lightest planet." % entry_number

# Style notes
# This is bad style - it is complex and unclear for other programmers.
def f(a, b, c):
    if a:
        if b:
            print 'hi'
        elif c:
            print 'bonjour'
        else:
            print 'hola'
    else:
        print 'Select a language'

# This is much clearer:
def f(a, b, c):
    if a and b:
        print 'hi'
    elif a and c:
        print 'bonjour'
    elif a:
        print 'hola'
    else:
        print 'Select a language'

