import re


def main():
    file = open("input.txt", "r")
    line_count = 0
    for line in file:
        line = line.strip()
        line_count += 1
        message = validate(line, line_count)
        print(message)


def validate(line, line_count):
    error_message = check_word(line, line_count)
    if error_message is not None:
        return error_message
    error_message = longer_than_previous(line, line_count)
    if error_message is not None:
        return error_message
    error_message = ends_with_dot(line, line_count)
    if error_message is not None:
        return error_message
    return "Sentence #{} is valid".format(line_count)


def ends_with_dot(line, line_count):
    if not line.endswith("."):
        return "Sentence #{} is invalid missing dot at the end.".format(line_count)


def check_word(line, line_count):
    if line.endswith("."):
        line = line[:-1]
    words = line.split()
    for word in words:
        word_index = words.index(word)
        word_position = word_index + 1
        word_pattern = "^" \
                       "(" \
                       "([bd]*[o]{{{}}}[bd]*[e]{{{}}}[bd]*)|" \
                       "([bd]*[e]{{{}}}[bd]*[o]{{{}}}[bd]*)|" \
                       "([bd]*)|" \
                       "([bd]*[o]{{{}}}[bd]*)|" \
                       "([bd]*[e]{{{}}}[bd]*)|" \
                       ")" \
                       "$".format(word_position, word_position, word_position, word_position, word_position, word_position)
        is_it_valid = re.findall(word_pattern, word)
        if len(is_it_valid) == 0:
            return "Sentence #{} word #{} is invalid.".format(line_count, word_index + 1)


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
