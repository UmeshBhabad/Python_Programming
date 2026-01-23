# Write a program which contains one function that accepts one number and check whether it is divisible by 5 or not.

###########################################################################
#
# Function Name :   DivisibleBy5
# Description   :   used to check whether it is divisible by 5 or not.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def DivisibleBy5(No):
    return No % 5 == 0

def main():
    bRet = False

    print("Enter the Number :")
    Val = int(input())

    bRet = DivisibleBy5(Val)

    print(bRet)

if __name__ == "__main__":
    main()