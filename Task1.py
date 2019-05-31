"""This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?"""

import os
import sys

def checkEntryIsSumOfTwoNumbersInList(list, k):
    for i in range(0,len(list)-1):
        if list[i] + list[i+1] == k:
            return True
    return False


if __name__== "__main__" :
    args = sys.argv
    listn = list(map(int,args[1].split(',')))    
    k = int(args[2])
    print(listn, k, checkEntryIsSumOfTwoNumbersInList(listn, k))

