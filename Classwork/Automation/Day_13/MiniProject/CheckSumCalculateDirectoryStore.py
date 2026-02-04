import os
import hashlib

def CalculateCheckSum(dirName):    
    fobj = open(dirName, 'rb')

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("There is no such Directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a Directory")
        return
    
    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    return Duplicate

def DisplayResult(MyDict):
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    count = 0

    for value in Result:
        for subvalue in value:
            count += 1
            print(subvalue)

        print("Value of Count is : ",count)
        count = 0

def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            count += 1
            print(subvalue)

            if count > 1 :
                print("Deleted File : ", subvalue)
                os.remove(subvalue)
                Cnt += 1

        count = 0

    print("Total deleted files : ", Cnt)

def main():
    
    DeleteDuplicate()

if __name__ == "__main__":
    main()