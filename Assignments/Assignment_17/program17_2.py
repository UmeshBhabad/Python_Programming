# Write a program which accept one number and display below pattern.
'''
    Input   :   5
    Output  :   *   *   *   *   *
                *   *   *   *   *
                *   *   *   *   *
                *   *   *   *   *
                *   *   *   *   *
'''

###########################################################################
#
# Function Name :   Display
# Description   :   used to print pattern on screen.
# Input         :   int
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def Display(No):
    for i in range(No):
        for j in range(No):
            print("*", end = "\t")
        print()

def main():
    
    print("Enter the Number :")
    Val = int(input())

    Display(Val)

if __name__ == "__main__":
    main()