# Write a program which that accepts a number and display grades.

###########################################################################
#
# Function Name :   Display
# Description   :   used to prints grades.
# Input         :   Int
# Output        :   str
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def Display(No):
    
    if No >= 75:
        print("Distinction")
    elif No >= 60:
        print("First class")
    elif No >= 50:
        print("Second Class")
    else:
        print("Fail")

def main():

    print("Enter the Marks :")
    Val = int(input())

    Display(Val)

if __name__ == "__main__":
    main()