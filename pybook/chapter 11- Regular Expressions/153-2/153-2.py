import re


def main():
    file_name = input("Enter a file name: ")
    file = open(file_name, "r")
    count = 0
    total = 0
    for line in file:
        line = line.rstrip()
        number_match = re.findall("^New Revision: ([0-9]+)", line)
        if number_match:
            count += 1
            total += int(number_match[0])
    print(total / count)


main()
