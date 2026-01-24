# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
'''
Input: Number of elements: 7

Input Elements: 13  5   45  7   4   56  34

Output: 5
'''

###########################################################################
#
# Function Name :   Minimum
# Description   :   Return Minimum number from that List.
# Input         :   list
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def Minimum(Lst):
    Min = Lst[0]

    for i in Lst:
        if i < Min:
            Min = i

    return Min

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

    Ret = Minimum(Data)

    print("Minimum of elements is", Ret)

if __name__ == "__main__":
    main()