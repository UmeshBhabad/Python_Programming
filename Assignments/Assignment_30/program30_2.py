# Count Words in a File
'''
Problem Statement:

Write a program which accepts a file name from the user and counts the total number of words in that file.

Input:

Demo.txt

Expected Output:

Total number of words in Demo.txt.
'''

import os

def main():
    FileName = ""
    Lst = []
    Count = 0

    print("Enter the name of file")
    FileName = input()

    if not (os.path.exists(FileName)):
        print("There is no such file")
        return

    fobj = open(FileName , 'r')

    Data = fobj.read()

    Lst = Data.split(" ")

    for s in Lst:        
        Count = Count + 1

    print("Total number of words in file : ", Count)

    # print(Data)
    

if __name__ == "__main__":
    main()