# Write a program which accept one number and returns addition of digits in that number.
'''
    Input   :   5187934
    Output  :   7
'''

###########################################################################
#
# Function Name :   SumDigits
# Description   :   used to addition digits in the number.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def SumDigits(No):
    sum = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        No //= 10
        sum += Digit

    return sum

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = SumDigits(Val)

    print("Sum of digits in", Val, "is", Ret)

if __name__ == "__main__":
    main()