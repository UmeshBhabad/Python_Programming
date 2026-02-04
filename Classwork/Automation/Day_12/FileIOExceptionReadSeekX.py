# seek(offset, when)
# seek(Kuthe, Kuthun)
# Futhun : 0/ 1/ 2
# 0 : Starting
# 1 : Current
# 2 : End

# Note : File should be opened in binary mode to perform various seek operations 

# Main Method
def main():
    try:                                                        # opens file if present
        fobj = open("Hello.txt", "r")
        print("File gets sucessfully opened")

        print("Current offset is : ", fobj.tell())  # 0
        
        fobj.seek(7, 0)     # same as seek(7)                   # sets offset to 7

        print("Current offset is : ", fobj.tell())  # 7

        Data = fobj.read(10)                                    # reads 10 bytes

        print("Current offset is : ", fobj.tell())  # 17

        print("Data from file is : ",Data)

        fobj.close()                                            # closes file

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")
        
# Start of the program
if __name__ == "__main__":
    main()