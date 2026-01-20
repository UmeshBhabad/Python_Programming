# Write a program which that accepts one number and check whether it is prime or not.

###########################################################################
#
# Function Name :   ChkPrime
# Description   :   used to check whether the given number is prime or not.
# Input         :   Integer
# Output        :   Boolean
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def ChkPrime(No):
    bFlag = False

    for i in range(2, No // 2):
        if(No % i == 0):
            bFlag = True
            break

    return bFlag

def main():
    bRet = False

    print("Enter the Number :")
    Val = int(input())

    bRet = ChkPrime(Val)

    if(bRet == False):
        print("Prime")
    else:
        print("Not Prime")

if __name__ == "__main__":
    main()