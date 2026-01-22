# Write a lambda function using filter() which accepts a list of strings and returns list of strings having length greater than 5.

###########################################################################
#
# Function Name :   Size
# Description   :   used to check whether the string lenth is greater than 5.
# Input         :   str
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   22/01/2026
#
###########################################################################

Size = lambda str1 : len(str1) > 5

def main():
    Data = list()

    print("Enter the number of elements :")
    Length = int(input())

    print("Enter elements :")
    for _ in range(Length):
        Val = input()

        Data.append(Val)

    print("Elements :")
    print(Data)

    # print("Enter elements :")
    # Data = list(map(int, input().split()))

    FData = list(filter(Size,Data))
    
    print(FData)

if __name__ == "__main__":
    main()