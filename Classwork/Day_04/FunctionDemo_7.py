# Accept : Multiple Parameters
# Return : one Value
def Marvellous1(Value1, Value2):    # Positional Argument
    print("Inside Marvellous1 : ", Value1, Value2)
    return 11

def main():
    Result = None

    Result = Marvellous1("Python", 21)

    print("Return Value is : ", Result)

if __name__ == "__main__":
    main()
