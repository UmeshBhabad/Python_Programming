# Write a program which contains one function named as Add() which accepts two numbers and returns the addition of two numbers.

###########################################################################
#
# Function Name :   Add
# Description   :   used to find the sum of two numbers.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def Add(No1, No2):
    return No1 + No2

def main():
    Ret = 0

    print("Enter the first Number :")
    Val1 = int(input())

    print("Enter the second Number :")
    Val2 = int(input())

    Ret = Add(Val1, Val2)

    print("Sum of numbers is :", Ret)

if __name__ == "__main__":
    main()