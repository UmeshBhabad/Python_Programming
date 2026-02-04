def multiplication(iValue1, iValue2):
    Ans = 0         # Local Variable
    Ans = iValue1 * iValue2
    return Ans

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Result = multiplication(No1, No2)
    print("Multiplication is : ", Result)

# Starter
if __name__ == "__main__":
    main()