def main():
    file = open("input.txt", "r")
    word_count = dict()
    for line in file:
        scanner(word_count, line)
    bigger_than_zero(word_count)


def scanner(word_count, line):
    if line.startswith("ADD"):
        line = line[4:-1]
        if line in word_count:
            word_count[line] += 1
        else:
            word_count[line] = 1
    else:
        line = line[7:-1]
        if line in word_count:
            word_count[line] -= 1
        else:
            word_count[line] = -1


def bigger_than_zero(dictionary):
    for key in dictionary:
        if dictionary[key] > 0:
            print(key, dictionary[key])


main()
