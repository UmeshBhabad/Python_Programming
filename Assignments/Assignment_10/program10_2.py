# Write a program which that accepts one number and print the sum of first N natural numbers.

###########################################################################
#
# Function Name :   Summation
# Description   :   used to find the sum of first N natural numbers.
# Input         :   Integer
# Output        :   Integer
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def Summation(No):
    sum = 0

    for i in range(1,No + 1):
        sum += i

    return sum

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = Summation(Val)

    print("Sum of first", Val, "natural numbers :", Ret)

if __name__ == "__main__":
    main()