import re


def main():
    file = open("input.txt", "r")
    word_list = []
    corresponding_count = []
    for line in file:
        line = re.sub(r'[^\w\s]', '', line)
        words = line.lower().split()
        for word in words:
            if word not in word_list:
                word_list.append(word)
                corresponding_count.append(1)
            else:
                word_position = word_list.index(word)
                corresponding_count[word_position] += 1

    for x in range(len(word_list)):
        print(word_list[x], corresponding_count[x])


main()
