# Reading specific number of bytes from the file

# Main Method
def main():
    try:                                                        # opening file if present
        fobj = open("Hello.txt", "r")
        print("File gets sucessfully opened")

        Data = fobj.read(6)                                     # reading 6 bytes from file

        print("Data from file is : ",Data)

        fobj.close()                                            # closing file

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")
        
# start of the program
if __name__ == "__main__":
    main()