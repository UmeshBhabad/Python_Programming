# writing in a file

# Main Method
def main():
    try:                                                        # Opens file if present else creates new file
        fobj = open("Hello.txt", "w")
        print("File gets sucessfully opened")

        fobj.write("Jay Ganesh Marvellous...")                  # writing given str in file

        fobj.close()                                            # closing file

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

# Start of program
if __name__ == "__main__":
    main()