# Copy File Contents into Another File
'''
Problem Statement:

Write a program which accepts two file names from the user.

First file is an existing file

Second file is a new file

Copy all contents from the first file into the second file.

Input:
    ABC.txt Demo.txt

Expected Output:
    Contents of ABC.txt copied into Demo.txt.
'''

import os

def main():
    SrcName = ""
    DestName = ""
    Buffer = bytes()
    Lst = []
    Count = 0

    print("Enter the name of Source file : ")
    SrcName = input()

    print("Enter the name of Destination file : ")
    DestName = input()

    if not (os.path.exists(SrcName)):
        print("There is no such file")
        return

    srcobj = open(SrcName , 'r')

    destobj = open(DestName, 'w')

    Buffer = srcobj.read()

    destobj.write(Buffer)

    print("File copied sucessfully")

    # print(Data)
    

if __name__ == "__main__":
    main()