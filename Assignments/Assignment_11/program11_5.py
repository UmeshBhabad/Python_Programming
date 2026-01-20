# Write a program which that accepts one number and checks whether it is palindrome or not.

###########################################################################
#
# Function Name :   ChkPalindrome
# Description   :   used to check if given number is palindrome or not.
# Input         :   Integer
# Output        :   Boolean
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def ChkPalindrome(No):
    NewNum = 0
    iDigit = 0

    OldNum = No

    while(No != 0):
        iDigit = No % 10
        No //= 10
        NewNum = NewNum * 10 + iDigit

    if NewNum == OldNum:
        return True
    else:
        return False

def main():
    bRet = 0

    print("Enter the Number :")
    Val = int(input())

    bRet = ChkPalindrome(Val)

    if(bRet):
        print("Palindrome")
    else:
        print("Not a Palindrome")

if __name__ == "__main__":
    main()