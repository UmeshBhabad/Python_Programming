# Write a program which that accepts one number and checks whether if is perfect number or not.

###########################################################################
#
# Function Name :   PerfectNum
# Description   :   used to check if number is perfect or not.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

import math

def PerfectNum(No):
    sum = 0

    for i in range(1, (No // 2) + 1):
        if No % i == 0:
            sum += i

    if sum == No:
        return True
    else:
        return False

def main():
    bRet = False

    print("Enter the number :")
    Val = int(input())

    bRet = PerfectNum(Val)

    if(bRet):
        print("Perfect Number.")
    else:
        print("Not a Perfect Number.")

if __name__ == "__main__":
    main()