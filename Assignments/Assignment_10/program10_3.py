# Write a program which that accepts one number and print the factorial of that number.

###########################################################################
#
# Function Name :   Factorial
# Description   :   used to find the factorial of that number.
# Input         :   Integer
# Output        :   Integer
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def Factorial(No):
    iFact = 1

    for i in range(1, No + 1):
        iFact *= i

    return iFact

# def Factorial(No):
#     if No == 1:
#         return 1
    
#     return No * Factorial(No - 1)

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = Factorial(Val)

    print("Factorial of", Val, "is", Ret)

if __name__ == "__main__":
    main()