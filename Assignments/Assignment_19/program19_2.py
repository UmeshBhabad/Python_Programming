# Write a program which contains one lambda function which accepts two parameters and return its multiplication.
'''
Input: 4    3

Output: 12

Input: 6    3

Output: 18
'''

###########################################################################
#
# Function Name :   Mult
# Description   :   return multiplication of two numbers.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

Mult = lambda No1, No2 : No1 * No2

def main():
    Ret = 0

    print("Enter the first number :")
    Val1 = int(input())

    print("Enter the second number :")
    Val2 = int(input())

    Ret = Mult(Val1, Val2)

    print("Multiplication of two numbers is :", Ret)

if __name__ == "__main__":
    main()