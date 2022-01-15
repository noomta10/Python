from main import print_error_for_line


def test():
    file = open("test.txt", "r")
    line_count = 0
    for line in file:
        line = line.strip()
        line_count += 1
        line = line.split(" - ")
        print_error_for_line(line[0], line_count)


test()