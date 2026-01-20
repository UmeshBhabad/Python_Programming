# Write a program which that accepts two number and prints its addition, substraction, multiplication, division.

###########################################################################
#
# Function Name :   ArithOp
# Description   :   used to prints addition substraction, multiplication and division of given numbers.
# Input         :   int
# Output        :   str
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def ArithOp(No1, No2):
    
    print("Addition :", No1 + No2)
    print("Substraction :", No1 - No2)
    print("Multiplication :", No1 * No2)
    print("Division :", No1 / No2)

def main():

    print("Enter the first number :")
    Val1 = int(input())

    print("Enter the second number :")
    Val2 = int(input())

    ArithOp(Val1, Val2)

if __name__ == "__main__":
    main()