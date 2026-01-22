# Write a lambda function using map () which accepts a list of numbers and returns list of squares of each number.

###########################################################################
#
# Function Name :   Square
# Description   :   used to return square of the number.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

Square = lambda No : No ** 2

def main():
    Data = list()

    print("Enter the number of elements :")
    Length = int(input())

    print("Enter elements :")
    for _ in range(Length):
        Val = int(input())

        Data.append(Val)

    print("Elements :")
    print(Data)
    
    # print("Enter elements :")
    # Data = list(map(int, input().split()))

    MData = list(map(Square,Data))

    print(MData)

if __name__ == "__main__":
    main()