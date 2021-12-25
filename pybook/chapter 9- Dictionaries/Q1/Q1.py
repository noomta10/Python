import string


def main():
    file = open("input.txt", "r")
    words_counts = dict()
    for line in file:
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation)).lower()
        words = line.split()
        for word in words:
            counter(word, words_counts)
    print(words_counts)


def counter(word, words_counts):
    if word not in words_counts:
        words_counts[word] = 1
    else:
        words_counts[word] += 1


main()
