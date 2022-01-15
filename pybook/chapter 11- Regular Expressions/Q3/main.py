import re
from collections import Counter


def main():
    file = open("input.txt", "r")
    line_count = 0
    for line in file:
        line = line.rstrip()
        line_count += 1
        print_error_for_line(line, line_count)


def print_error_for_line(line, line_count):
    check = check_word(line, line_count)
    if not check:
        return
    double = double_word(line, line_count)
    if not double:
        return
    longer = longer_than_previous(line, line_count)
    if not longer:
        return
    ends = ends_with_dot(line, line_count)
    if not ends:
        return


def ends_with_dot(line, line_count):
    if not line.endswith("."):
        print("Sentence #{} missing dot at the end.".format(line_count))
        return False


def check_word(line, line_count):
    word_pattern = "^[bd]*$"
    line = line.split()
    for item in line:
        is_it_valid = re.findall(word_pattern, item)
        if len(is_it_valid) == 0:
            print("Sentence #{} word is invalid ".format(line_count))
            return False


def longer_than_previous(line, line_count):
    line = line.split()
    for item_index, item in enumerate(line):
        if item_index == len(line) - 1:
            continue
        if len(item) < len(line[item_index + 1]):
            continue
        else:
            print("Sentence #{} word must be longer than previous.".format(line_count))
            return False


def double_word(line, line_count):
    line = line.split()
    occurrences_count = Counter(line)
    for occurrences in occurrences_count.values():
        if occurrences > 1:
            print("Sentence #{} word #{} exists more than once".format(line_count,
                                                                       (occurrences_count[occurrences] + 1)))
            return False


if __name__ == '__main__':
    main()
