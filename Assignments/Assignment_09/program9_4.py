# Write a program which that accepts one number and print cube of that number.

###########################################################################
#
# Function Name :   NumCube
# Description   :   used to find cube of a number.
# Input         :   Integer
# Output        :   Integer
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def NumCube(No):
    return No ** 3

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = NumCube(Val)

    print("Cube of the number is", Ret)

if __name__ == "__main__":
    main()