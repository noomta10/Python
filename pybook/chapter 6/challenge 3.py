def replace_once(line):
    duplicate_position = line.find("duplicate")
    space_position = line.find(" ", duplicate_position)
    number = int(line[space_position + 1])
    word_position = line.find(" ", space_position + 1)
    word_end = line.find(" ", word_position + 1)
    if word_end == -1:
        word = line[word_position + 1:]
        word = word + " "
        return line[:duplicate_position] + word * number
    else:
        word = line[word_position + 1:word_end]
        word = word + " "
        return line[:duplicate_position] + word * number + line[word_end + 1:]


def main():
    sentence = input("write a sentence: ")
    while "duplicate" in sentence:
        sentence = replace_once(sentence)
    print(sentence)


main()
