# greedy.py
  
# Ryan Raishart on 6/3/2017
# rraishart@gmail.com
  
# Finds the fewest coins needed
# for a given amount of change.

import cs50


# Gets valid change amount
def getChange():
    while True:
        print("How much change is owed?")
        cents = cs50.get_float()
        if cents > -1.0:
            break
    return cents


# Returns amount of coins needed    
def getCoins(change):
    coins = 0
    QUARTER = 25
    while change >= QUARTER:
        change -= QUARTER
        coins += 1
    DIME = 10
    while change >= DIME:
        change -= DIME
        coins += 1
    NICKEL = 5
    while change >= NICKEL:
        change -= NICKEL
        coins += 1
    PENNY = 1
    while change >= PENNY:
        change -= PENNY
        coins += 1
    return coins
    
    
    
# Converts dollars to cents and rounds
def convertCents(amount):
    rounded = amount * 100
    rounded = round(rounded)
    return rounded


def main():
    change = getChange()
    cents = convertCents(change)
    coins = getCoins(cents)
    print(coins)
    

main()