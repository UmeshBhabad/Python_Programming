# Write a program which that accepts one number and check whether it is divisible by 3 and 5.

###########################################################################
#
# Function Name :   Divisible
# Description   :   used to check if given number is divisible by 3 and 5.
# Input         :   Integer
# Output        :   Boolean
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def Divisible(No):
    bFlag = False

    if No % 3 == 0 & No % 5 == 0:
        bFlag = True

    return bFlag 

def main():
    Ret = False

    print("Enter the Number :")
    Val = int(input())

    Ret = Divisible(Val)

    if(Ret):
        print("Number is divisible by 3 and 5.")
    else:
        print("Number is not divisible by 3 and 5.")

if __name__ == "__main__":
    main()