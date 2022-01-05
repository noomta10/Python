import re


def main():
    file = open("mbox-short.txt", "r")
    regular_expression = input("Enter a regular expression: ")
    count = 0
    for line in file:
        if re.search(regular_expression, line):
            count += 1
    print("mbox-short.txt had {} lines that matched {}".format(count, regular_expression))


main()
