import time

def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact *= i

    return Fact

def main():
    Value = int(input("Enter Number : "))
    Ret = 0

    start_time = time.time()
    Ret = Factorial(Value)
    end_time = time.time()

    print("factorial is ", Ret)

    print("Total Execution time is ", end_time - start_time)

if __name__ == "__main__":
    main()