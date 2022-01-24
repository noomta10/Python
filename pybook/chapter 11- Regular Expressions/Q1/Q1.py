import re


def main():
    file = open("Input.html", "r")
    for line in file:
        line = line.strip()
        sentence_match = re.findall("<div>(.*?)</div>", line)
        if sentence_match:
            for match in sentence_match:
                print(match, end=" ")
            print()


main()
