# Write a program which display 10 to 1 on screen.

###########################################################################
#
# Function Name :   fun
# Description   :   used to print 10 to 1 on screen.
# Input         :   None
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def fun():
    for i in range(10, 0, -1):
        print(i, end = "\t")

def main():
    fun()

if __name__ == "__main__":
    main()