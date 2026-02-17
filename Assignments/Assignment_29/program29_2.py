# Display File Contents
'''
Problem Statement:

Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

Input:

Demo.txt

Expected Output:

Display contents of Demo.txt on console.
'''

import os

def main():
    FileName = ""
    Ret = False

    print("Enter the name of the file")
    FileName = input()

    Ret = os.path.exists(FileName) and os.path.isfile(FileName)

    if Ret == False :
        print("There is no such file.")
        return
    
    fobj = open(FileName, 'r')

    Data = fobj.read()

    print(Data)

if __name__ == "__main__":
    main()