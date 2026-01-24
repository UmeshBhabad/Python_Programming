# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.
'''
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 

List after filter = [2, 4, 4, 2, 8, 10] 

List after map = [4, 16, 16, 4, 64, 100]

Output of reduce = 204
'''

from functools import reduce

###########################################################################
#
# Function Name :   isEven
# Description   :   checks whether the number is even.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

isEven = lambda No : No % 2 == 0

###########################################################################
#
# Function Name :   Square
# Description   :   used to square the given number.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

Square = lambda No: No ** 2

###########################################################################
#
# Function Name :   Add
# Description   :   Return Addition of two numbers.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

Add = lambda No1, No2: No1 + No2

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

    FData = list(filter(isEven, Data))
    
    print("List after filter : ", end = "")
    print(FData)
    
    MData = list(map(Square, FData))
    
    print("List after map :", end = "")
    print(MData)

    Ret = reduce(Add, MData)

    print("output of reduce is", Ret)

if __name__ == "__main__":
    main()