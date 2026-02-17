# Display File Line by Line
'''
Problem Statement:

Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

Input:
    Demo.txt

Expected Output:
    T Display each line of Demo.txt one by one.
'''

import os

def main():
    FileName = ""
    Buffer = bytes()
    Lst = []
    Count = 0

    print("Enter the name of file")
    FileName = input()

    if not (os.path.exists(FileName)):
        print("There is no such file")
        return

    fobj = open(FileName , 'r')

    Buffer = fobj.read()

    print(str(Buffer))

    # print(Data)
    

if __name__ == "__main__":
    main()