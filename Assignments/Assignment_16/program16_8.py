# Write a program which that accepts one number from user and prints that number of '*' on screen.

###########################################################################
#
# Function Name :   Display
# Description   :   used to print that number of '*' on screen.
# Input         :   int
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def Display(No):
    for i in range(No):
        print("*", end = "\t")

def main():
    
    print("Enter the Number :")
    Val = int(input())

    Display(Val)

if __name__ == "__main__":
    main()