# Write a lambda function using filter() which accepts a list of numbers and returns list of Odd number.

###########################################################################
#
# Function Name :   Odd
# Description   :   used to whether the number is Odd.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

Odd = lambda No : No % 2 == 1

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

    FData = list(filter(Odd,Data))
    
    print(FData)

if __name__ == "__main__":
    main()