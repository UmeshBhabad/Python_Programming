import sys
import os

def DirectoryScanner(dirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(dirName)

    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(dirName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName, SubFolder, FileName in os.walk(dirName):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            print("File Name : ", fname)
            print("File Size : ", os.path.getsize(fname))       # path issue

def main():
    Border = "-"*50

    print(Border)
    print("------- Marvellous Directory Automation ----------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print('Please specify the name of Directory')
        return

    DirectoryScanner(sys.argv[1])

if __name__ == "__main__":
    main()