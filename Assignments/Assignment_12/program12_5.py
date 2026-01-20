# Write a program which that accepts a number and prints that many numbers in reverse order.

###########################################################################
#
# Function Name :   Display
# Description   :   used to prints natural numbers in reverse.
# Input         :   Int
# Output        :   str
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def Display(No):
    
    for i in range(No, 0, -1):
        print(i, end = "\t")

def main():

    print("Enter the first number :")
    Val = int(input())

    Display(Val)

if __name__ == "__main__":
    main()