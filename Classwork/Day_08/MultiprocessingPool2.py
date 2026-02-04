
def sumCube(No):
    sum = 0

    for i in range(1, No + 1):
        sum += (i**3)

    return sum

def main():
    Ret = 0

    Ret = sumCube(10)

    print(Ret)

if __name__ == "__main__":
    main()