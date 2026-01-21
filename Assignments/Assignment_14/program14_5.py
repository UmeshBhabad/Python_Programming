# Write a lambda function which accepts one number and returns True if number else is even otherwise False.

###########################################################################
#
# Function Name :   IsEven
# Description   :   used to returns True if number else is even otherwise False.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

IsEven = lambda No : No % 2 == 0

def main():
    bRet = False

    print("Enter the first number :")
    Val = int(input())

    bRet = IsEven(Val)

    if(bRet):
        print("Even")
    else:
        print("Odd")    

if __name__ == "__main__":
    main()