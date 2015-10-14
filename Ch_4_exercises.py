# Exercises for Chapter 4

import math
print "The absolute rounded value of -4.3 is %f." % (abs(round(-4.3)))
print "The ceiling of the sin of 34.5 is %f." % (math.ceil(math.sin(34.5)))

import calendar
print "The number of leap years between 2000 and 2050 is %d." % (calendar.leapdays(2000, 2050))
print "The day of the week of July 29, 2016 is %d" % (calendar.weekday(2016, 07, 29))

print 'boolean'.capitalize()
print 'C02 H20'.find('2') # It is 2, as Python indices start at 0
print 'C02 H20'.find('2', 3)
print 'C02 H20'.find('2', 'C02 H20'.find('2') + 1)
print 'Boolean'[0].isupper() # First letter of Boolean is uppercase
print "MoNDaY".lower().upper()
print "   Monday".strip()


