import sys

def process_file(filename):
    '''Open, read, and print a file.'''
    
    input_file = open(filename, "r")
    for line in input_file:
        line = line.strip()
        print line
    input_file.close()
if __name__ == "__main__": # If this is running from the command line
    process_file(sys.argv[1]) # take the argument 'filename' as the second argument