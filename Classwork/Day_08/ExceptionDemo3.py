
def main():
    Ans = 0

    try:
        print("Inside try")
        
        print("Enter first Number :")
        No1 = int(input())

        print("Enter second Number :")
        No2 = int(input())    
        
        Ans = No1 / No2
    
    except ZeroDivisionError as zobj:
        print("Inside except : ", zobj)

    except ValueError as vobj:
        print("Inside except : ",vobj)

    except Exception as eobj:                   # Generic Exception
        print("Inside except : ", eobj)

    finally:
        print("Inside finally")

    print("Division is : ", Ans)

if __name__ == "__main__":
    main()