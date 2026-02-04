# Procedural Approach

def CheckEven(No):
    
    if(No % 2 == 0):
        print("It is Even.")
    else:
        print("It is Odd.")

def main():
    CheckEven(21)       # positional argument
    CheckEven(No = 22)  # Keyword Argument

if __name__ == "__main__":
    main()