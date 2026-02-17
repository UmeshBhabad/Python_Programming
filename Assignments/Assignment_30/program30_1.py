# Count Lines in a File
'''
Problem Statement:

Write a program which accepts a file name from the user and counts how many lines are present in the file.

Input:
    Demo.txt

Expected Output:
    Total number of lines in Demo.txt.
'''

import os

def main():
    FileName = ""
    Count = 0

    print("Enter the name of file")
    FileName = input()

    if not (os.path.exists(FileName)):
        print("There is no such file")
        return

    fobj = open(FileName , 'r')

    Data = fobj.read()

    if(len(Data) != 0):
            Count = 1

    for s in Data:
        if s == '\n':
            Count = Count + 1

    print("Total number of lines in Demo.txt : ", Count)

    # print(Data)
    

if __name__ == "__main__":
    main()