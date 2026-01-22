# Write a lambda function using reduce() which accepts a list of numbers and returns addition of all elements.

###########################################################################
#
# Function Name :   Add
# Description   :   used to add numbers.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################
from functools import reduce

Add = lambda No1, No2 : No1 + No2 

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

    RData = reduce(Add,Data)
    
    print(RData)

if __name__ == "__main__":
    main()