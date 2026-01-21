# Write a lambda function which accepts one number and returns cube of that number.

###########################################################################
#
# Function Name :   Cube
# Description   :   used to return Cube of the number.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

Cube = lambda No : No ** 3

def main():
    Ret = 0

    print("Enter the number :")
    Val = int(input())

    Ret = Cube(Val)

    print("Cube of the number is :", Ret)

if __name__ == "__main__":
    main()