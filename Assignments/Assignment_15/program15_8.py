# Write a lambda function using filter() which accepts a list of numbers and returns list of number divisible by 3 and 5.

###########################################################################
#
# Function Name :   Divisible
# Description   :   used to check whether the number is divisible by 3 and 5.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

Divisible = lambda No : No % 3 == 0 and No % 5 == 0

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

    FData = list(filter(Divisible,Data))
    
    print(FData)

if __name__ == "__main__":
    main()