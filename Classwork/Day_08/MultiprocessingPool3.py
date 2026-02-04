import os
import time

def sumCube(No):
    print("Process is running with PID : ", os.getpid())

    sum = 0

    for i in range(1, No + 1):
        sum += (i**3)

    return sum

def main():
    Ret = 0
    Result = list()

    Data = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000]

    start_time = time.time()

    for i in range(len(Data)):
        Ret = sumCube(Data[i])

        Result.append(Ret)

    end_time = time.time()

    print(Result)
    print("Total Execution time : ", end_time - start_time)

if __name__ == "__main__":
    main()