# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers, List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
'''
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45,70]

List after filter = [76, 89, 86, 90, 70]

List after map [86, 99, 96, 100, 80]

Output of reduce = 6538752000
'''

from functools import reduce

###########################################################################
#
# Function Name :   Increment
# Description   :   used to increase each number by 10.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

Increment = lambda No: No + 10

###########################################################################
#
# Function Name :   Large
# Description   :   checks whether the number is greater than or equal to 70 and less than or equal to 90..
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

Large = lambda No : No >= 70 and No <= 90

###########################################################################
#
# Function Name :   Product
# Description   :   Return multiplication of two numbers.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

Product = lambda No1, No2: No1 * No2

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

    FData = list(filter(Large, Data))
    
    print("List after filter : ", end = "")
    print(FData)
    
    MData = list(map(Increment, FData))
    
    print("List after map :", end = "")
    print(MData)

    Ret = reduce(Product, MData)

    print("product of  elements is", Ret)

if __name__ == "__main__":
    main()