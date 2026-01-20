# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.

###########################################################################
#
# Function Name :   ChkGreater
# Description   :   used to find greater number between two numbers.
# Input         :   Two Integers
# Output        :   Integer
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def ChkGreater(No1, No2):
    if(No1 > No2):
        return No1
    else:
        return No2

def main():
    Ret = 0

    print("Enter first Number :")
    Val1 = int(input())

    print("Enter second Number :")
    Val2 = int(input())

    Ret = ChkGreater(Val1, Val2)

    print("Greater number is", Ret)

if __name__ == "__main__":
    main()