# Main Method
def main():
    try:                                                        # opening file if present
        fobj = open("Hello.txt", "r")
        print("File gets sucessfully opened")

        print("Current offset is : ", fobj.tell())
        
        Data = fobj.read(6)                                     # reading file

        print("Current offset is : ", fobj.tell())

        print("Data from file is : ",Data)

        fobj.close()                                            # closing file

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")
        
# Start of the program
if __name__ == "__main__":
    main()