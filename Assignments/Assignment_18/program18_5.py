# Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().
'''
Input: Number of elements: 11

Input Elements: 13  5   45  7   4   56  10  34  2   5   8

Output: 32
'''

from MarvellousNum import ChkPrime
from functools import reduce

###########################################################################
#
# Function Name :   Add
# Description   :   Return addition of two numbers.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

Add = lambda No1, No2: No1 + No2

def main():
    Data = list()

    print("Enter the number of elements :")
    Length = int(input())

    print("Enter elements :")
    for _ in range(Length):
        Val = int(input())

        Data.append(Val)

    print("Elements :")
    print(Data)

    FData = list(filter(ChkPrime, Data))
    
    print("Prime Numbers : ")
    print(FData)

    Ret = reduce(Add, FData)

    print("Sum of Prime elements is", Ret)

if __name__ == "__main__":
    main()