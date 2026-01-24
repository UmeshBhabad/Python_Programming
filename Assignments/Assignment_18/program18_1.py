# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
'''
Input: Number of elements: 6

Input Elements: 13  5   45  7   4   56

Output: 130
'''

###########################################################################
#
# Function Name :   Summation
# Description   :   used to find addition of all elements from that List.
# Input         :   list
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def Summation(Lst):
    sum = 0

    for i in Lst:
        sum += i

    return sum

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

    Ret = Summation(Data)

    print("Summation of elements is", Ret)

if __name__ == "__main__":
    main()