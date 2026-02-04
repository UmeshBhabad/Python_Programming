# Reading data from file

# Main Method
def main():
    try:                                                        # opening file if present
        fobj = open("Hello.txt", "r")
        print("File gets sucessfully opened")

        Data = fobj.read()                                      # reading data

        print("Data from file is : ",Data)

        fobj.close()                                            # closing file

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")
        
# Start of program
if __name__ == "__main__":
    main()