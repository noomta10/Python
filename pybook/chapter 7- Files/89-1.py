def main():
    file_name = input("Enter a file name: ")
    try:
        file_name = open(file_name)
    except:
        print("File can not be opened", file_name)
        exit()

    for line in file_name:
        line = line.rstrip()
        print(line.upper())


main()
