def main():
    file = open("input.txt", "r")
    first_line = int(input("enter a line: "))
    first_word = int(input("enter the first word: "))
    width = int(input("enter a width: "))
    height = int(input("enter a height: "))
    lines = []
    for line in file:
        lines.append(line)
    for rectangle_line_index in range(height):
        print_rectangle_line(first_line, lines, rectangle_line_index, first_word, width)


def print_rectangle_line(first_line, lines, rectangle_line_index, first_word, width):
    line_index = rectangle_line_index + first_line
    if line_index < len(lines):
        line = lines[line_index]
    else:
        line = ''
    print_rectangle_word(line, width, first_word)
    print()


def print_rectangle_word(line, width, first_word):
    words = line.split()
    for rectangle_word_index in range(width):
        word_index = rectangle_word_index + first_word
        if word_index < len(words):
            print(words[word_index], end=" ")
        else:
            print("x", end=" ")


main()
