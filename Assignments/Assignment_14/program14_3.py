# Write a lambda function which accepts two number and returns maximum number.

###########################################################################
#
# Function Name :   Maximum
# Description   :   used to return Maximum of the number.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    Ret = 0

    print("Enter the first number :")
    Val1 = int(input())

    print("Enter the second number :")
    Val2 = int(input())

    Ret = Maximum(Val1, Val2)

    print("Maximum is :", Ret)    

if __name__ == "__main__":
    main()