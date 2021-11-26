import re


def main():
    file = open("input.txt", "r")
    word_list = []
    corresponding_count = []
    for line in file:
        line_counter(word_list, corresponding_count, line)
    for x in range(len(word_list)):
        print(word_list[x], corresponding_count[x])


def line_counter(my_words, my_counts, line):
    line = re.sub(r'[^\w\s]', '', line)
    words = line.lower().split()
    for word in words:
        if word not in my_words:
            my_words.append(word)
            my_counts.append(1)
        else:
            word_position = my_words.index(word)
            my_counts[word_position] += 1

main()
