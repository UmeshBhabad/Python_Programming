# Write a program which that accepts one number and print all odd numbers till that number.

###########################################################################
#
# Function Name :   DisplayOdd
# Description   :   used to print all the Odd numbers till the given number.
# Input         :   Integer
# Output        :   Integers
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def DisplayOdd(No):

    for i in range(1, No + 1, 2):
        print(i, end = "\t")

def main():

    print("Enter the Number :")
    Val = int(input())

    DisplayOdd(Val)

if __name__ == "__main__":
    main()