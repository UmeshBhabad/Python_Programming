# Write a program which contains one lambda function which accepts one parameter and return power of two.
'''
Input: 4

Output: 16

Input: 6

Output: 64
'''

###########################################################################
#
# Function Name :   PowerOf2
# Description   :   used to return square of the number.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

PowerOf2 = lambda No : No ** 2

def main():
    Ret = 0

    print("Enter the number :")
    Val = int(input())

    Ret = PowerOf2(Val)

    print("Square of the number is :", Ret)

if __name__ == "__main__":
    main()