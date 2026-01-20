# Write a program which that accepts one number and prints binary equivalent.

###########################################################################
#
# Function Name :   Binary
# Description   :   used to print binary representation of the given number.
# Input         :   int
# Output        :   str
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def Binary(No):
    Bin = list()
    Binary = ""
    Digit = 0

    while (No != 0):
        Digit = No % 2
        Bin.append(Digit)
        No = No // 2

    for i in range(len(Bin) - 1, -1, -1):
        Binary += str(Bin[i])

    print(Binary)

def main():

    print("Enter the number :")
    Val = int(input())

    Binary(Val)

if __name__ == "__main__":
    main()