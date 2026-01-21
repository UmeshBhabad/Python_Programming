# Write a lambda function which accepts three number and returns largest number.

###########################################################################
#
# Function Name :   Largest
# Description   :   used to return Largest of the number.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

Largest = lambda No1, No2, No3 : No1 if No1 >= No2 and No1 >= No3 else (No2 if No2 >= No1 and No2 >= No3 else No3)

def main():
    Ret = 0

    print("Enter the first number :")
    Val1 = int(input())

    print("Enter the second number :")
    Val2 = int(input())

    print("Enter the third number :")
    Val3 = int(input())

    Ret = Largest(Val1, Val2, Val3)

    print("Largest is :", Ret)    

if __name__ == "__main__":
    main()