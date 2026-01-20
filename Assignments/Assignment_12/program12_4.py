# Write a program which that accepts a number and prints that many numbers starting from 1.

###########################################################################
#
# Function Name :   Display
# Description   :   used to prints natural numbers.
# Input         :   Int
# Output        :   str
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def Display(No):
    
    for i in range(1, No + 1):
        print(i, end = "\t")

def main():

    print("Enter the first number :")
    Val = int(input())

    Display(Val)

if __name__ == "__main__":
    main()