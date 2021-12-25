import re


def main():
    file_name = input('Enter the file name: ')
    file = open(file_name, "r")
    letters = {}
    for line in file:
        line = line.lower()
        line = re.sub('[^a-z]', '', line)
        letter_counter(line, letters)
    dictionary_to_list(letters)


def letter_counter(line, letters):
    for letter in line:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1


def dictionary_to_list(letters):
    letters_list = []
    for letter, letter_count in letters.items():
        letters_list.append((letter, letter_count))
    letters_list.sort()
    all_letters_count = 0

    for _, letter_count in letters_list:
        all_letters_count = all_letters_count + letter_count

    for letter, letter_count in letters_list:
        print(letter, letter_count * 100 / all_letters_count)


main()
