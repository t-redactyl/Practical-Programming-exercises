# Practical Programming Chapter 6 notes

# Boolean operators
not True
not False

# If both are true, 'and' statements are true, and false otherwise
True and True
True and False

# If either are True, 'or' statements are true, and false otherwise
True or True
True or False
False or False

# Relational operators
3 < 5 # True
13 >= 77 # False

def positive(x):
    return x > 0

# Order of operations
1 + 3 < 7 # (1 + 3) < 7 = 4 < 7
x = 3
(1 < x) and (x <= 5)
1 < x <= 5

# Applying booleans to integers, floats and strings
# Numbers - 0 is false, all other numbers are true
not 0 # True
not 1 # False

# 'and' and numbers
# Lazy evaluating - stops evaluating once it gets to false or the end of the expression
# Returns either the first false expression or the final value
0 and 3
3 and 0
3 and 5

# 'or' and numbers
# Stops evaluating once it gets to the first 'true' expression or the end of the expression
# Returns first true value or last value in expression
1 or 0
0 or 1
0 or False or 18
0 or True or 18

# Strings - are represented 'under the hood' by integers, so these are used
# to evaulate greater than/less than statements
'A' < 'a'

# Empty string is false, all other strings are true
'' and False
False or 'salmon'

# True and False are represented by numbers
False == 0 # False is 0
True == 1
False < True

# if statements
ph = float(raw_input())
if ph < 7.0:
    print "%s is acidic." % ph

ph = float(raw_input())
if ph < 7.0:
    print "%s is acidic." % ph
if ph > 7.0:
    print "%s is basic." % ph
    
ph = float(raw_input())
if ph < 7.0:
    print "%s is acidic." % ph
elif ph > 7.0:
    print "%s is basic." % ph

# Using elif is faster, as it will only be evaluated if the first if statement is false.

compound = raw_input("Enter compound: ")
if compound == "H20":
    print "Water"
elif compound == "NH3":
    print "Ammonia"
elif compound == "CH4":
    print "Methane"
else:
    print "Unknown compound"
    
# Nested if statements
input = raw_input("> ")
if len(input) > 0:
    ph = float(input)
    if ph < 7.0:
        print "%s is acidic." % ph
    elif ph > 7.0:
        print "%s is basic." % ph
    else:
        print "%s is neutral." % ph
else:
    print "No pH value was given!"
    
# Storing conditionals

