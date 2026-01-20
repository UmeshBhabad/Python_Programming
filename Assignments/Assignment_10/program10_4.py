# Write a program which that accepts one number and print all even numbers till that number.

###########################################################################
#
# Function Name :   DisplayEven
# Description   :   used to print all the even numbers till the given number.
# Input         :   Integer
# Output        :   Integers
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def DisplayEven(No):

    for i in range(2, No + 1, 2):
        print(i, end = "\t")

def main():

    print("Enter the Number :")
    Val = int(input())

    DisplayEven(Val)

if __name__ == "__main__":
    main()