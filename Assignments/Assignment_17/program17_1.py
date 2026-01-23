'''Create on module named as Arithmetic which contains 4 functions as Add() for addition,
Sub() for subtraction, Mult() for multiplication and Div() for division. 
All functions accepts two parameters as number and perform the operation. 
Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.'''

import Arithematic

def main():
    Ret = 0

    print("Enter the first Number :")
    Val1 = int(input())

    print("Enter the second Number :")
    Val2 = int(input())

    Ret = Arithematic.Add(Val1, Val2)
    print("Addition is", Ret)

    Ret = Arithematic.Sub(Val1, Val2)
    print("Substraction is", Ret)

    Ret = Arithematic.Mult(Val1, Val2)
    print("Multiplication is", Ret)

    Ret = Arithematic.Div(Val1, Val2)
    print("Division is", Ret)

if __name__ == "__main__":
    main()