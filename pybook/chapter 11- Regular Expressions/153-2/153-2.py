import re


def main():
    file_name = input("Enter a file name: ")
    file = open(file_name, "r")
    count = 0
    total = 0
    for line in file:
        line = line.rstrip()
        if re.findall("^New Revision: ([0-9]+)", line):
            dfddd = re.findall("^New Revision: ([0-9]+)", line)
            count += 1
            total += int(dfddd[0])
    print(total / count)


main()
