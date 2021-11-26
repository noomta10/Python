def main():
    file = open("mbox-short.txt", "r")
    line_count = 0
    for line in file:
        if line.startswith("From "):
            words = line.split()
            print(words[1])
            line_count += 1
    print("There were {} lines in the file with From as the first word".format(line_count))

main()