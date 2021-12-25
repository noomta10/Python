import string


def main():
    file = open("input.txt", "r")
    words_locations = dict()
    line_index = 1
    for line in file:
        line = line.rstrip().lower().translate(line.maketrans('', '', string.punctuation))
        words = line.split()
        for word_index, word in enumerate(words):
            word_index += 1
            add_location(word, words_locations, line_index, word_index)
        line_index += 1
    print_locations(words_locations)


def add_location(word, words_locations, line_index, word_index):
    item = "line: {} word: {} ".format(line_index, word_index)
    if word in words_locations:
        words_locations[word].append(item)
    else:
        words_locations[word] = [item]


def print_locations(dictionary):
    for key in dictionary:
        print(key + ": ", end="")
        for item in (dictionary[key]):
            print(item, end="")
        print()


main()
