# Write a program which that accepts one number and prints count of digits in that number.

###########################################################################
#
# Function Name :   CountDigits
# Description   :   used to count digits in the given number.
# Input         :   Integer
# Output        :   Integer
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def CountDigits(No):
    Count = 0

    while(No != 0):
        No //= 10
        Count += 1

    return Count

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = CountDigits(Val)

    print("Count of Digits is :", Ret)

if __name__ == "__main__":
    main()