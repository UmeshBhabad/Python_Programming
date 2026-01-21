# Write a lambda function which accepts one number and returns True if number is divisible by 5.

###########################################################################
#
# Function Name :   DivisibleBy5
# Description   :   used to returns True returns True if number is divisible by 5.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

DivisibleBy5 = lambda No : No % 5 == 0

def main():
    bRet = False

    print("Enter the first number :")
    Val = int(input())

    bRet = DivisibleBy5(Val)

    if(bRet):
        print("number is divisible by 5")
    else:
        print("number is not divisible by 5")    

if __name__ == "__main__":
    main()