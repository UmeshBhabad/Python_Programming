# Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
'''
Input: Number of elements: 11

Input Elements: 13  5   45  7   4   56  5   34  2   5   65

Element to search : 5

Output: 3
'''

###########################################################################
#
# Function Name :   Frequency
# Description   :   return frequency of the given number from List.
# Input         :   list, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def Frequency(Lst, No):
    Count = 0

    for i in Lst:
        if i == No:
            Count += 1

    return Count

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

    print("Enter the element to search :")
    Value = int(input())

    Ret = Frequency(Data, Value)

    print("Frequency of element", Value, "is", Ret)

if __name__ == "__main__":
    main()