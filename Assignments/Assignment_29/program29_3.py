# Copy File Contents into a New File (Command Line)
'''
Problem Statement:

Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.

Input (Command Line):

ABC.txt

Expected Output:

Create Demo.txt and copy contents of ABC. txt into Demo.txt.
'''

import os

def main():
    SrcFileName = ""
    DestFileName = ""

    Buffer = ""

    Ret = False

    print("Enter the name of the source file : ")
    SrcFileName = input()

    print("Enter the name of the Destination file : ")
    DestFileName = input()

    Ret = os.path.exists(SrcFileName) and os.path.isfile(SrcFileName)

    if Ret == False :
        print("There is no such file.")
        return
    
    Sfobj = open(SrcFileName, 'r')

    Data = Sfobj.read()

    Dfobj = open(DestFileName, 'w')

    Dfobj.write(Data)

if __name__ == "__main__":
    main()