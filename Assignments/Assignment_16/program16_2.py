# Write a program which contains on function named as ChkNum() which accepts one number as parameter. If number is even then it should display "Even number" otherwise display "Odd number" on console.

###########################################################################
#
# Function Name :   ChkNum
# Description   :   used to check whether the given number is even or not.
# Input         :   Integer
# Output        :   Boolean
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def ChkNum(No):
    return No % 2 == 0

def main():
    bRet = False

    print("Enter the Number :")
    Val = int(input())

    bRet = ChkNum(Val)

    if(bRet):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()