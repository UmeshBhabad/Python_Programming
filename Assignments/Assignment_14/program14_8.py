# Write a lambda function which accepts two number and returns addition.

###########################################################################
#
# Function Name :   Addition
# Description   :   used to return addition of the numbers.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

Addition = lambda No1, No2 : No1 + No2

def main():
    Ret = 0

    print("Enter the first number :")
    Val1 = int(input())

    print("Enter the second number :")
    Val2 = int(input())

    Ret = Addition(Val1, Val2)

    print("Addition is :", Ret)    

if __name__ == "__main__":
    main()