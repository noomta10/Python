def main():
    prefixes = {}
    file = open("input.txt", "r")
    for line in file:
        line = line.split()
        for item in line:
            find_prefixes(item, prefixes)
    print(prefixes)


def find_prefixes(item, prefixes):
    for index in range(len(item)):
        prefix = item[0:index + 1]
        if prefix not in prefixes:
            prefixes[prefix] = 1
        else:
            prefixes[prefix] += 1
        index += 1


main()
