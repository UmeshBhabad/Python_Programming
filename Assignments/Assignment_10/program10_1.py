# Write a program which that accepts one number and print multiplication table of that number.

###########################################################################
#
# Function Name :   MultTable
# Description   :   used to print multiplaication table of a number.
# Input         :   Integer
# Output        :   Integer
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def MultTable(No):
    print("Multiplication Table of", No)

    for i in range(1,11):
        print(No, "*", i, "=", No * i)

def main():
    
    print("Enter the Number :")
    Val = int(input())

    MultTable(Val)


if __name__ == "__main__":
    main()