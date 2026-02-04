import os

def DirectoryScanner(DirectoryName = "Marvellous"):
    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such Directory")
        return

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("Unable to scan as it is not directory")
        return
    
    print("Contents of the  directory are : ")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder Name : ", FolderName)

        for SubF in SubFolderName:
            print("Sub Folder Name : ", SubF)

        for fname in FileName:
            print("File Name : ", fname)

def main():
    DirectoryName = input("Enter the name of Directory : ")

    
    DirectoryScanner(DirectoryName)
    

if __name__ == "__main__":
    main()