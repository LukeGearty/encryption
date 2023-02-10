#!/usr/bin/env python3
## import statements
import sys

#### dictionaries for comparison ######

dict_one = {
    'A':1,   #1
    'B':2,  #2
    'C':3,  #3
    'D':4,  #4
    'E':5,  #5
    'F':6,  #6
    'G':7,  #7
    'H':8,  #8
    'I':9,  #9
    'J':10, #10
    'K':11, #11
    'L':12, #12
    'M':13, #13
}

dict_two = {
    'N':1,  #14
    'O':2,  #15
    'P':3,   #16
    'Q':4,  #17
    'R':5,  #18
    'S':6,  #19
    'T':7,  #20
    'U':8,  #21
    'V':9,  #22
    'W':10, #23
    'X':11, #24
    'Y':12, #25
    'Z':13, #26
}

#### helper functions #####



def rot13(word:str):

    #a variable for the encrypted word
    encrypted = ""
    for char in word:

        #compare char to the letters in dict_one and dict_two

        if char.upper() in dict_one.keys():
            comparison = dict_one[char.upper()]
            for key,value in dict_two.items():
                if value == comparison:
                    encrypted += str(key)
        elif char.upper() in dict_two.keys():
            comparison = dict_two[char.upper()]
            for key,value in dict_one.items():
                if value == comparison:
                    encrypted += str(key)
        elif char == " ":
            encrypted += char

    print(encrypted.lower())
#### main function ######
def main():
    arg = sys.argv[1]
    rot13(arg)

#### dunder check ####
if __name__=="__main__":
    main()
   
#### if the message is longer than one word it should be in quotes ######
