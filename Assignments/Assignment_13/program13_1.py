# Write a program which that accepts length and width of rectangle and print area.

###########################################################################
#
# Function Name :   Area
# Description   :   used to return area of rectangle.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def Area(l, w):
    
    return l * w

def main():
    Ret = 0

    print("Enter the length :")
    Val1 = int(input())

    print("Enter the width :")
    Val2 = int(input())

    Ret = Area(Val1, Val2)

    print("Area of Rectangle :", Ret)

if __name__ == "__main__":
    main()