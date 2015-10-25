# Practical Programming Chapter 12 notes

# Breaking down code into functions that can be resued makes programs more
# efficient.
# Default parameter values are a way of making it easier to generalise programs.
import sys
sys.path.insert(0, "/Users/jburchell/Documents/Practical-Programming-exercises/Scripts from book")
from default_define import total
numbers = [10, 20, 30]
print "total(numbers, 0, 3):", total(numbers, 0, 3)
print "total(numbers, 2):", total(numbers, 2)
print "total(numbers):", total(numbers)

# Variable arguments
def our_max(*values):
    '''Find the maximum of any number of values.'''
    
    if not values:
        return None
    m = values[0]
    for v in values[1:]:
        if v > m:
            m = v
    return m

# Note the *values argument - values does not have to be a single value:
print our_max(1)
print our_max(1, 2)
print our_max(2, 1, 2, 5, 4, -17)

# The * tells Python to take all of the arguments, put them in a tuple, and 
# assign that tuple to the variable values.

# Starred parameters can also be combined with other arguments, but must go at 
# the end of the argument list. Python will then assign all of the leftover
# parameters to it.

def append_all(old, *new):
    for n in new:
        old.append(n)
    return old

values = []
print append_all(values, 1, 2, 3)
print append_all(values) # Not actually passing argument to new.

# However, you cannot have more than one starred argument in a single function,
# as the assignment would be ambiguous.

# Named parameters
# You can assign names to parameters so you can call them in any order you like
# (or if a parameter has a default, you can skip it)

def describe_creature(name, species, age, weight):
    return '%s (%s): %d years, %d kg' % (name, species, age, weight)

print describe_creature(name = 'Charles Darwin', species = 'Homo sapiens',
                        age = 28, weight = 70)

# Exceptions
try:
    x = 1 / 0.3
    print 'reciprocal of 0.3 is', x
    x = 1 / 0.0
    print 'reciprocal of 0.0 is', x
except:
    print 'error: no reciprocal'
    
# If nothing goes wrong in try section, all of the program is executed and the
# except block is skipped. If any exceptions are 'raised' in the try block,
# Python jumps to the start of the except block and executes all of the code
# inside it (the 'exception has been caught'). The code that deals with 
# exceptions is called an 'exception handler'. Statements in the try block
# after the statement that raised the exception are not executed.

def invert(x):
    try:
        i = 1.0 / x
    except:
        print 'caught exception for', x
    else:
        print 'reciprocal of', x, 'is', i
        
invert(1)
invert(0)

# Exception objects
# When exceptions are raised, objects are created the hold information about
# what went wrong.

values = [1, 0, 1]
for i in range(4):
    try:
        r = 1.0 / values[i]
        print 'reciprocal of', values[i], 'at', i, 'is', r
    except IndexError:
        print 'index', i, 'out of range'
    except ArithmeticError:
        print 'unable to calculate reciprocal of', values[i]

# Using default Python error messages        
values = [-1, 0, 1]
for i in range(4):
    try:
        r = 1.0 / values[i]
        print 'reciprocal of', values[i], 'at', i, 'is', r
    except IndexError, e:
        print 'error:', e
    except ArithmeticError, e:
        print 'error:', e

# If you don't write your own exception handler, Python will attempt to draw
# from its inbuilt exception handlers

# Raising exceptions

def divide(top, bottom):
    if bottom == 0:
        raise ValueError('divisor is zero')
    else:
        return top / bottom

for i in range(-1, 2):
    try:
        print divide(1, i)
    except ValueError, e:
        print 'caught exception for', i

# Patterns
# How a program is organised is important for readibility and maintenance.
# Fixed values go at the top of the program.

SECONDS_PER_DAY = 24 * 60 * 60
instant = 10**3
while instant <= 10**7:
    print "%10d seconds is %8.2f days" % \
          (instant, (1.0 * instant / SECONDS_PER_DAY))
    instant *= 10

# The most-wanted holder is a value that is closest to what we want (e.g.,
# maximum value in a list)

# Most-recent holder holds the value most recently seen from some sequence
# of values.

# A container is a value that holds other values.

whole = 'selenium'
for i in range(len(whole)/2):
    print whole
    whole = whole[1:-1]
    
# A gatherer/accumulator collects individual values (e.g., a variable 'result'
# would be a gatherer if it collected the sum of a list of values).

# A temporary is a variable that exists for only a short time.

# A one-way flag is a variable whose value changes just once to show that
# something has occurred.

