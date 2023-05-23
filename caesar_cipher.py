#!/usr/bin/python3

# helper functions
def caesar(text,shift):
    encrypted = ""

    for char in text:
        if char.isalpha() and char.isupper(): # checking if the character is an uppercase letter
            text = int(ord(char))
            offset = text + shift
            encrypted += chr(offset)
        elif char.isalpha() and char.islower(): # checking if the character is lowercase
             text = int(ord(char))
             offset = text + shift
             encrypted += chr(offset)
        else: # in case there's punctuation
            encrypted += char
    return encrypted
            


# main function

def main():
    text = str(input("Enter the text you wish to encrypt: "))
    shift = int(input("Enter the shift amount: "))
    print(caesar(text,shift))


if __name__=="__main__":
    main()
