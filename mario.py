# mario.py

# Ryan Raishart on 6/3/2017
# rraishart@gmail.com
 
# Prints Mario-esque pyramid of a given size.

import cs50

def main():
    size = getInput()
    height = size - 2
    blocks = 2
    print(size)
    
    for i in range(size):
        printSpace(height)
        printHash(blocks)
        height -= 1
        blocks += 1
        print(" ")
        
def getInput():
    while True:
        print("enter pyramid size")
        n = cs50.get_int()
        if n > -1 and n < 24:
            break
    return n

def printHash(hashes):
    for i in range(hashes):
        print("#", end=" ")
        
def printSpace(spaces):
    for i in range(spaces + 1):
        print(" ", end =" ")
main()