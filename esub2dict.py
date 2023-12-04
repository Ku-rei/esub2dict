#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:      #check that the user provided only one argument (the text file), if not exit with error code 1
        print("Something is wrong with the arguments. You need to provide the filename after the program's name")
        sys.exit(1)
    '''sys.argv is 1 if the script/program executes with no additional arguments (aside for the name of the scrip)
    +1 for any other argument, like the text file name here'''    


    userfile = sys.argv[1] #takes the command line argument and assigns it a variable "userfile"
    

    with open(userfile, 'r') as file:   # use "with" to avoid deadlocks in case the program crashes 
        # data = file.read() # Creates a string of all the file. N.B it moves the pointer file to the end of the file!!
        
        for line in file:
            print(line, end='')  # Just for testing, remove later.
