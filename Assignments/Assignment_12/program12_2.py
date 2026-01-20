# Write a program which that accepts one number and prints its factors.

###########################################################################
#
# Function Name :   Factors
# Description   :   used to prints factors of given number.
# Input         :   int
# Output        :   str
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def Factors(No):
    for i in range(1, No + 1):
        if(No % i == 0):
            print(i, end = " ")

def main():

    print("Enter the number :")
    Val = int(input())

    Factors(Val)

if __name__ == "__main__":
    main()