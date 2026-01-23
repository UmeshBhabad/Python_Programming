# Write a program which that accepts one number and check whether it is prime or not.

###########################################################################
#
# Function Name :   ChkNum
# Description   :   used to check whether the given number is positive, negative or zero.
# Input         :   int
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def ChkNum(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    print("Enter the Number :")
    Val = int(input())

    ChkNum(Val)

if __name__ == "__main__":
    main()