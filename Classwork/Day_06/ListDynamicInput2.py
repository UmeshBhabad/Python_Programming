def main():
    Size = 0
    Value = 0
    Sum = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    for i in range(Size):
        Sum += Data[i]

    print("Summation is : ",Sum)
    
if __name__ == "__main__":
    main()