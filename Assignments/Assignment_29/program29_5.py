# Frequency of a String in File
'''
Problem Statement:

Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

Input:
Demo.txt Marvellous

Expected Output:
Count how many times "Marvellous" appears in Demo.txt.
'''

import os
import sys

def main():
    FileName = ""
    Ret = False
    Count = 0

    str1 = sys.argv[2]

    FileName = sys.argv[1]

    Ret = os.path.exists(FileName) and os.path.isfile(FileName)

    if Ret == False :
        print("There is no such file.")
        return
    
    fobj = open(FileName, 'r')

    Data = fobj.read()

    Token = []

    Token = Data.split(" ")

    for s in Token:
        if(s == str1):
            Count += 1

    print("Count of occurance of \'Marvellous' is", Count)

if __name__ == "__main__":
    main()