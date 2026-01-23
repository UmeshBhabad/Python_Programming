# Write a program which that accepts one name from user and display length of its name.

###########################################################################
#
# Function Name :   Display
# Description   :   used to display length of given string.
# Input         :   str
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def Display(name):
    print(len(name))

def main():
    
    print("Enter the Number :")
    Val = input()

    Display(Val)

if __name__ == "__main__":
    main()