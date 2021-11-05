def main():
    file_name = input("Enter a file name: ")
    try:
        if file_name == "na na boo boo":
            print("NA NA BOO BOO")
            return
        else:
            file = open(file_name)
    except:
        print("File can not be opened", file_name)
        exit()

    total = 0
    for line in file:
        if line.startswith("Subject"):
            total += 1
    print("There were " + str(total) + " subject lines in " + file_name)


main()

