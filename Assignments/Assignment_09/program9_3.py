# Write a program which that accepts one number and print square of that number.

###########################################################################
#
# Function Name :   NumSquare
# Description   :   used to find square of a number.
# Input         :   Integer
# Output        :   Integer
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def NumSquare(No):
    return No ** 2

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = NumSquare(Val)

    print("Square of the number is", Ret)

if __name__ == "__main__":
    main()