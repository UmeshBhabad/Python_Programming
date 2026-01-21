# Write a lambda function which accepts one number and returns True if number else is even otherwise False.

###########################################################################
#
# Function Name :   IsOdd
# Description   :   used to returns True if number else is odd otherwise False.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

IsOdd = lambda No : No % 2 == 1

def main():
    bRet = False

    print("Enter the first number :")
    Val = int(input())

    bRet = IsOdd(Val)

    if(bRet):
        print("Odd")
    else:
        print("Even")    

if __name__ == "__main__":
    main()