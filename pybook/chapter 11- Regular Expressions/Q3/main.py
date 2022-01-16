import re


def main():
    file = open("input.txt", "r")
    line_count = 0
    for line in file:
        line = line.rstrip()
        line_count += 1
        msg = validate(line, line_count)
        print(msg)


def validate(line, line_count):
    check = check_word(line, line_count)
    if check is not None:
        return check
    longer = longer_than_previous(line, line_count)
    if longer is not None:
        return longer
    ends = ends_with_dot(line, line_count)
    if ends is not None:
        return ends
    return "Sentence #{} is valid".format(line_count)


def ends_with_dot(line, line_count):
    if not line.endswith("."):
        return "Sentence #{} is invalid missing dot at the end.".format(line_count)
    else:
        return


def check_word(line, line_count):
    if line.endswith("."):
        line = line[:-1]
    words = line.split()
    for word in words:
        word_index = words.index(word)
        word_pattern = "^" \
                       "(" \
                       "([bd]*[o]{{{}}}[e]{{{}}}[bd]*)|" \
                       "([bd]*)|" \
                       "([bd]*[o]{{{}}}[bd]*)|" \
                       "([bd]*[e]{{{}}}[bd]*)|" \
                       ")" \
                       "$".format(
            (word_index + 1), (word_index + 1), (word_index + 1), (word_index + 1))
        is_it_valid = re.findall(word_pattern, word)
        if len(is_it_valid) == 0:
            return "Sentence #{} word #{} is invalid.".format(line_count, word_index + 1)
        else:
            return


def longer_than_previous(line, line_count):
    if line.endswith("."):
        line = line[:-1]
    words = line.split()
    for item_index, item in enumerate(words):
        if item_index == len(words) - 1:
            return
        if len(item) >= len(words[item_index + 1]):
            return "Sentence #{} word must be longer than previous.".format(line_count)


if __name__ == '__main__':
    main()
