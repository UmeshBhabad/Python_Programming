# Search a Word in File
'''
Problem Statement:

Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

Input:
    Demo.txt Marvellous

Expected Output:
    Display whether the word Marvellous is found in Demo. txt or not.
'''

import os

def main():
    FileName = ""
    Word = ""
    Lst = []
    Count = 0

    print("Enter the name of file : ")
    FileName = input()

    print("Enter the word to find : ")
    Word = input()

    if not (os.path.exists(FileName)):
        print("There is no such file")
        return

    fobj = open(FileName , 'r')

    Data = fobj.read()

    Lst = Data.split(" ")

    for s in Lst:        
        if(s == Word):
            Count = Count + 1

    print(f"Total count of word '{Word}' in file :  {Count}")

    # print(Data)
    

if __name__ == "__main__":
    main()