import re


def main():
    file = open("Input.html", "r")
    for line in file:
        line = line.rstrip()
        if re.search("^<div>(.*)</div>", line):
            sentence = re.findall("^<div>(.*)</div>", line)
            print(sentence[0])


main()
