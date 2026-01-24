# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
'''
Input List = [2, 70, 11, 10, 17, 23, 31, 77] 
List after filter = [2, 11, 17, 23, 31] 
List after map = [4, 22, 34, 46, 62]

Output of reduce = 62
'''

from functools import reduce

###########################################################################
#
# Function Name :   isPrime
# Description   :   checks whether the number is prime or not.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

def isPrime(No):
    for i in range(2, (No // 2) + 1):
        if No % i == 0:
            return False
    return True

###########################################################################
#
# Function Name :   MultBy2
# Description   :   used to multiply the given number by 2.
# Input         :   int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

MultBy2 = lambda No: No * 2

###########################################################################
#
# Function Name :   Maximum
# Description   :   Return Maximum of two numbers.
# Input         :   int, int
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   24/01/2026
#
###########################################################################

Maximum = lambda No1 , No2: No1 if No1 > No2 else No2

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

    FData = list(filter(isPrime, Data))
    
    print("List after filter : ", end = "")
    print(FData)
    
    MData = list(map(MultBy2, FData))
    
    print("List after map :", end = "")
    print(MData)

    Ret = reduce(Maximum, MData)

    print("output of reduce is", Ret)

if __name__ == "__main__":
    main()