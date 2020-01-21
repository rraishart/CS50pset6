# caesar.py
# Ryan Raishart on 4/13/2016
# rraishart@gmail.com
# Encrypts messages using Caesar's cipher.

import cs50
import sys


def Encrypt(phrase, key):
    ALPHA_SIZE = 26
    CAP_A_ASCII = 65
    LOW_A_ASCII = 97
    n = CAP_A_ASCII
    j = LOW_A_ASCII
    alpha = []
    lowalpha = []
    for x in range(ALPHA_SIZE): # store alphabet as ascii
        alpha.append(n)
        n = n + 1
    
    for z in range(ALPHA_SIZE):
        lowalpha.append(j)
        j = j + 1
    cText = []    
    
    for y in range(len(phrase)): # encrypt letters
        if phrase[y].isalpha() == False:
            cText.append(phrase[y])
        else:
            if phrase[y].islower():
                letter = ((ord(phrase[y]) - LOW_A_ASCII) + key) % ALPHA_SIZE
                cText.append(chr(lowalpha[letter]))
            else:
                letter = ((ord(phrase[y]) - CAP_A_ASCII) + key) % ALPHA_SIZE
                cText.append(chr(alpha[letter]))
    return cText
        

def main():
    if len(sys.argv) != 2:
        print("Usage: python caesar.py k")
        return 1
    key = int(sys.argv[1])    
    print("plaintext: ", end='')
    pText = cs50.get_string()
    newMessage = Encrypt(pText, key)
    print("ciphertext: ", end = "")
    for x in range(len(newMessage)):
        print(newMessage[x], end = "")
    print("")
main()