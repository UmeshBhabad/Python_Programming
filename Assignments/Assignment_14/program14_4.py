# Write a lambda function which accepts two number and returns minimum number.

###########################################################################
#
# Function Name :   Minimum
# Description   :   used to return Minimum of the number.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

Minimum = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Ret = 0

    print("Enter the first number :")
    Val1 = int(input())

    print("Enter the second number :")
    Val2 = int(input())

    Ret = Minimum(Val1, Val2)

    print("Minimum is :", Ret)    

if __name__ == "__main__":
    main()