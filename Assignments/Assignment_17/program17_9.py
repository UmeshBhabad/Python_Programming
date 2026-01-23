# Write a program which accept one number and returns number of digits in that number.
'''
    Input   :   5187934
    Output  :   7
'''

###########################################################################
#
# Function Name :   CountDigits
# Description   :   used to count digits in the number.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def CountDigits(No):
    Count = 0

    while(No != 0):
        No //= 10
        Count += 1

    return Count

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = CountDigits(Val)

    print("Number of digits in", Val, "is", Ret)

if __name__ == "__main__":
    main()