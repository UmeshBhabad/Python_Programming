# Write a lambda function using filter() which accepts a list of numbers and returns the count of even number.

###########################################################################
#
# Function Name :   CountEven
# Description   :   used to whether the number is even.
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

CountEven = lambda No : No % 2 == 0

def main():
    Data = list()
    Count = 0

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

    FData = list(filter(CountEven,Data))

    Count = len(FData)
    print("Count of even element is",Count)

if __name__ == "__main__":
    main()