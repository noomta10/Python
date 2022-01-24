from main import validate


def test():
    file = open("test.txt", "r")
    line_count = 0
    for line in file:
        line = line.strip()
        line_count += 1
        line = line.split(" - ")
        message = validate(line[0], line_count)
        if message == line[-1]:
            print("As expected.")
        else:
            print("Not as expected, printed {} supposed to print {}".format(message, line[1]))


test()
