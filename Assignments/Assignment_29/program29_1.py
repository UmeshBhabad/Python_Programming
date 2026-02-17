# Check File Exists in Current Directory
'''
Problem Statement:

Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

Input:

Demo.txt

Expected Output:

Display whether Demo.txt exists or not.
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
    else:
        print("File is present.")

if __name__ == "__main__":
    main()