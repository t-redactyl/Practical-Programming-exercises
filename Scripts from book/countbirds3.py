'''This program counts all birds in file birdwatching.txt, and then outputs the
count of birds by alphabetical order. It is designed to be used at the command
line.'''

import sys

# Count all the birds.
count = {}
for filename in sys.argv[1:]:
    infile = open(filename, "r")
    for line in infile:
        name = line.strip()
        count[name] = count.get(name, 0) + 1
    infile.close()

# Print
for b in sorted(count):
    print b, count[b]