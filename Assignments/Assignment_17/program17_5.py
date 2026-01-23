# Write a program which that accepts one number from the user and check whether it is prime or not.

###########################################################################
#
# Function Name :   ChkPrime
# Description   :   used to check whether the given number is prime or not.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
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
        print("It is a Prime Number.")
    else:
        print("It is Not a Prime Number.")

if __name__ == "__main__":
    main()