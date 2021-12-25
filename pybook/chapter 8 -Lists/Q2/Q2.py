import re


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


def main():
    file = open("input.txt", "r")
    word_list = []
    corresponding_count = []
    for line in file:
        line_counter(word_list, corresponding_count, line)
    for word_index in range(len(word_list)):
        print(word_list[word_index], corresponding_count[word_index])


# main()


# def f1(number):
#     number = number + 1
#     print("Hello {}".format(number))
#
#
# f1(3)
#
# a = 10
# print("Welcome {}".format(a))
# f1(a)
# print("Bye {}".format(a))
#
#
# def f2(names):
#     names.append("last one")
#     print("washing {}".format(names))
#
#
# f2(['mimi'])
# toys = ['yoyo', 'boo']
# print("toys before {}".format(toys))
# f2(toys)
# print("toys after {}".format(toys))
