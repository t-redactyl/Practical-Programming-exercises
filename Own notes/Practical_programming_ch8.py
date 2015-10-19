# Practical Programming Chapter 8

# File formats - one record per line
input_file = open("hopedale.txt", "r")
for line in input_file:
    line = line.strip()
    print line
input_file.close()

# Files over the internet
# urlopen in urllib module opens online data
import urllib
url = "http://www-personal.buseco.monash.edu.au/~hyndman/TSDL/ecology1/hopedale.dat"
web_page = urllib.urlopen(url)
for line in web_page:
    line = line.strip()
    print line
web_page.close()
# Doesn't work as access to data banned.

import urllib
url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
web_page = urllib.urlopen(url)
for line in web_page:
    line = line.strip()
    print line
web_page.close()

# Changing so that data file is not hard coded
import sys

def process_file(filename):
    '''Open, read, and print a file.'''
    
    input_file = open(filename, "r")
    for line in input_file:
        line = line.strip()
        print line
    input_file.close()
if __name__ == "__main__":
    process_file(sys.argv[1])

# Beyond printing data
