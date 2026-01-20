# Write a program which that accepts radius of circle and prints area of circle.

###########################################################################
#
# Function Name :   Area
# Description   :   used to return area of circle.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

import math

def Area(r):
    
    return math.pi * r * r

def main():
    Ret = 0

    print("Enter the radius :")
    Val = int(input())

    Ret = Area(Val)

    print("Area of Circle :", Ret)

if __name__ == "__main__":
    main()