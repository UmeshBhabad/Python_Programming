# Write a lambda function which accepts two number and returns Minimum number.

###########################################################################
#
# Function Name :   Minimum
# Description   :   used to return Minimum of the number.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################
from functools import reduce

Minimum = lambda No1, No2 : No1 if No1 < No2 else No2

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

    RData = reduce(Minimum,Data)
    
    print(RData)    

if __name__ == "__main__":
    main()