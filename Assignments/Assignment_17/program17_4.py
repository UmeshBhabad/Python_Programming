# Write a program which accept one number form user and return addition of its factors.

###########################################################################
#
# Function Name :   AddFactors
# Description   :   used to find factorial of the given number.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def AddFactors(No):
    sum = 0

    for i in range(1, (No // 2) + 1):
        if(No % i == 0):
            sum += i

    return sum

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = AddFactors(Val)

    print("Sum of Factors of", Val, "is", Ret)

if __name__ == "__main__":
    main()