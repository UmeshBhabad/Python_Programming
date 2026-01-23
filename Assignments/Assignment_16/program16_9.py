# Write a program which display 10 even numbers on screen.

###########################################################################
#
# Function Name :   Display
# Description   :   used to display 10 even numbers on screen.
# Input         :   None
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def Display():
    for i in range(2, 21, 2):
        print(i, end = "\t")

def main():
    Display()

if __name__ == "__main__":
    main()