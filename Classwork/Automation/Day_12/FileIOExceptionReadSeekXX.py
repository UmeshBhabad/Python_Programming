# seek(offset, when)
# seek(Kuthe, Kuthun)
# Futhun : 0/ 1/ 2
# 0 : Starting
# 1 : Current
# 2 : End

# Main Method
def main():
    try:                                                            # opens file if present
        fobj = open("Hello.txt", "r")
        print("File gets sucessfully opened")

        print("Current offset is : ", fobj.tell())  # 0
        
        fobj.seek(6, 2)                                             # sets offset to end of file 

        print("Current offset is : ", fobj.tell())  # 11

        Data = fobj.read(6)                                         # reads 6 bytes from the file

        print("Current offset is : ", fobj.tell())  # 17

        print("Data from file is : ",Data)

        fobj.close()                                                # closes

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")
        

if __name__ == "__main__":
    main()