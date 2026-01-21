# Write a lambda function which accepts a number and returns squares of that number.

###########################################################################
#
# Function Name :   Square
# Description   :   used to return square of the number.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

Square = lambda No : No ** 2

def main():
    Ret = 0

    print("Enter the number :")
    Val = int(input())

    Ret = Square(Val)

    print("Square of the number is :", Ret)

if __name__ == "__main__":
    main()