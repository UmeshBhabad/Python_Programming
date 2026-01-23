# Write a program which accept one number from user and return its factorial.

###########################################################################
#
# Function Name :   Fact
# Description   :   used to find factorial of the given number.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def Fact(No):
    if No == 0:
        return 1
    
    return No * Fact(No - 1)

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = Fact(Val)

    print("Factorial of", Val, "is", Ret)

if __name__ == "__main__":
    main()