# Compare Two Files (Command Line)
'''
Problem Statement:

Write a program which accepts two file names through command line arguments and compares the contents of both files.

If both files contain the same contents. display Success

Otherwise display Failure

Input (Command Line):

    Demo.txt Hello.txt

Expected Output:

    Success OR Failure
'''

import os
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName, 'rb')

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def main():
    FileName1 = ""
    FileName2 = ""

    Buffer = ""

    print("Enter the name of the first file : ")
    FileName1 = input()

    print("Enter the name of the second file : ")
    FileName2 = input()

    if (os.path.exists(FileName1) and os.path.isfile(FileName1))== False:
        print("There is no such file.")
        return
    
    if (os.path.exists(FileName2) and os.path.isfile(FileName2))== False:
        print("There is no such file.")
        return
    
    CS1 = CalculateCheckSum(FileName1)

    CS2 = CalculateCheckSum(FileName2)

    if CS1 == CS2:
        print("Sucess")
    else:
        print("Failure")

if __name__ == "__main__":
    main()