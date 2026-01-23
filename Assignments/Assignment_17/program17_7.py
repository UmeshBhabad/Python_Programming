# Write a program which accept one number and display below pattern.
'''
    Input   :   5
    Output  :   1   2   3   4   5
                1   2   3   4   5
                1   2   3   4   5
                1   2   3   4   5
                1   2   3   4   5
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
    for i in range(1, No + 1):
        for j in range(1, No + 1):
            print(j, end = "\t")
        print()

def main():
    
    print("Enter the Number :")
    Val = int(input())

    Display(Val)

if __name__ == "__main__":
    main()