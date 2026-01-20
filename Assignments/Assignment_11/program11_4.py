# Write a program which that accepts one number and prints reverse of that number.

###########################################################################
#
# Function Name :   ReverseNum
# Description   :   used to reverse the given number.
# Input         :   Integer
# Output        :   Integer
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def ReverseNum(No):
    NewNum = 0
    iDigit = 0

    while(No != 0):
        iDigit = No % 10
        No //= 10
        NewNum = NewNum * 10 + iDigit

    return NewNum

def main():
    Ret = 0

    print("Enter the Number :")
    Val = int(input())

    Ret = ReverseNum(Val)

    print("Reverse number is :", Ret)

if __name__ == "__main__":
    main()