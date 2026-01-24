
###########################################################################
#
# Function Name :   ChkPrime
# Description   :   used to check whether the number is prime or not.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def ChkPrime(No):
    bFlag = True

    for i in range(2, (No // 2) + 1):
        if No % i == 0:
            bFlag = False
            break

    return bFlag