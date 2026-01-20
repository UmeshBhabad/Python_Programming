# Write a program which that accepts one number and prints sum of digits in that number.

###########################################################################
#
# Function Name :   SumDigits
# Description   :   used to find sum of digits in the given number.
# Input         :   Integer
# Output        :   Integer
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def SumDigits(No):
    Sum = 0
    iDigit = 0

    while(No != 0):
        iDigit = No % 10
        No //= 10
        Sum += iDigit

    return Sum

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = SumDigits(Val)

    print("Sum of Digits is :", Ret)

if __name__ == "__main__":
    main()