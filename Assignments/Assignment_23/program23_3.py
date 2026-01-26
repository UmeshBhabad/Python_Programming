# Write a Python program to implement a class named Numbers with the following specifications:
'''
The class should contain one instance variable:

    Value

Define a constructor (init) that accepts a number from the user and initializes Value.

Implement the following instance methods:

    ChkPrime()- returns True if the number is prime, otherwise returns False

    ChkPerfect()- returns True if the number is perfect, otherwise returns False

    Factors()- displays all factors of the number

    SumFactors()- returns the sum of all factors
    (You may use this method as a helper in ChkPerfect() if required)

Create multiple objects and call all methods.
'''


class Numbers:
    Value = 0

    def __init__(self, num):
        self.No = num
    
    def ChkPrime(self):
        for i in range(2, (self.No // 2) + 1):
            if self.No % i == 0:
                return False
            
        return True

    def ChkPerfect(self):
        sum = 0

        for i in range(1, (self.No // 2) + 1):
            if self.No % i == 0:
                sum += i
        
        return sum == self.No

    def Factors(self):
        print("Factors : ", end ="")
        for i in range(1, (self.No // 2) + 1):
            if self.No % i == 0:
                print(i, end = "\t")
        print()

    def SumFactors(self):
        sum = 0

        for i in range(1, (self.No // 2) + 1):
            if self.No % i == 0:
                sum += i
        return sum

def main():
    Ret = 0
    bRet = False

    Obj1 = Numbers(10)

    print("Number :",Obj1.No)

    bRet = Obj1.ChkPrime()
    
    if bRet:
        print("Number is prime")
    else:
        print("Number is not prime")
    
    bRet = Obj1.ChkPerfect()
    
    if bRet :
        print("Number is perfect")
    else:
        print("Number is not perfect")
    
    Obj1.Factors()
    
    Ret = Obj1.SumFactors()
    print("Sum of Factors :", Ret)

    ####################################################################################

    Obj2 = Numbers(13)

    print("Number :",Obj2.No)

    bRet = Obj2.ChkPrime()
    
    if bRet:
        print("Number is prime")
    else:
        print("Number is not prime")
    
    bRet = Obj2.ChkPerfect()
    
    if bRet:
        print("Number is perfect")
    else:
        print("Number is not perfect")
    
    Obj2.Factors()
    
    Ret = Obj2.SumFactors()
    print("Sum of Factors :", Ret)

    ####################################################################################

    Obj3 = Numbers(28)

    print("Number :",Obj3.No)

    bRet = Obj3.ChkPrime()
    
    if bRet:
        print("Number is prime")
    else:
        print("Number is not prime")
    
    bRet = Obj3.ChkPerfect()
    
    if bRet:
        print("Number is perfect")
    else:
        print("Number is not perfect")
    
    Obj3.Factors()
    
    Ret = Obj3.SumFactors()
    print("Sum of Factors :", Ret)

if __name__ == "__main__":
    main()