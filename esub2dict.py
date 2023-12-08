#!/usr/bin/env python3

def main(argum):
    if len(argum) != 2:      #check that the user provided only one argument (the text file), if not exit with error code 1
        print("Something is wrong with the arguments. You need to provide the filename after the program's name")
        sys.exit(1)
    '''sys.argv is 1 if the script/program executes with no additional arguments (aside for the name of the scrip)
    +1 for any other argument, like the text file name here'''    
    
    userfile = argum[1] #takes the command line argument and assigns it to a variable "userfile"

    allowed_char = ['-', "'", ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
    wordlist = []

    with open(userfile, 'r') as file:   # use "with" to avoid deadlocks in case the program crashes 
        # data = file.read() # Creates a string of all the file. N.B it moves the pointer file to the end of the file!!
        

        for line in file:
            for index in range(len(line)): # measures line length and goes through it, character by character
                if index < len(line) - 1:   # needed to avoid error: Python index going outside of the list
                    next = line[index + 1]  # names the next character
                    if line[index] == 'i' and (next == '>'):    # removes html tag. PROBLEM REMOVES OTHER 'i's
                          line = line.replace(line[index],' ')
                    if line[index] == '-' and (next == '-'):    # removes "-->" between srt timestamps
                          line = line.replace(line[index],' ')
                          line = line.replace(line[index+1],' ')
                    if line[index] == '-' and ((next not in allowed_char) or (next == ' ')):    # removes all other weird dashes
                          line = line.replace(line[index],' ')
                          line = line.replace(line[index+1],' ')
                
                if line[index] not in allowed_char: # removes all characters unless alphabetical or dash/apostrophe.
                    line = line.replace(line[index],' ')
            # print(line,end='\n')
            words = line.split()
            for i in words:
                 i = i.lower()
                 wordlist.append(i)  # can append only one word per time
        
        wordlist = list(set(wordlist))  # removes duplicates through a set. WHAT ABOUT NAMES?
        wordlist.sort() # sort the list alphabetically 

        print(str(len(wordlist)))
        for i in wordlist:
             print(str(i))

        print(str(len(wordlist)))

        for i in wordlist:
             if "'" in i:
                  print(i)


if __name__ == "__main__":
    import sys
    main(sys.argv)
    


   
    
    
    
    

    