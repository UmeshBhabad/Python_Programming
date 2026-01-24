# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
'''
Input: Number of elements: 7

Input Elements: 13  5   45  7   4   56  34

Output: 56
'''

###########################################################################
#
# Function Name :   Maximum
# Description   :   Return Maximum number from that List.
# Input         :   list
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def Maximum(Lst):
    Max = Lst[0]

    for i in Lst:
        if i > Max:
            Max = i

    return Max

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

    Ret = Maximum(Data)

    print("Maximum of elements is", Ret)

if __name__ == "__main__":
    main()