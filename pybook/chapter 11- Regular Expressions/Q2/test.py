from main import check_valid


def test():
    line_index = 0
    file = open("test.txt", "r")
    for line in file:
        line_index += 1
        line = line.split()
        formula = ' '.join(line[1:])
        is_it_valid = check_valid(formula)
        working = True
        if is_it_valid:
            if line[0] == "true":
                continue
            else:
                print("Expected to be invalid, found valid, line {}".format(line_index))
                working = False
                break

        else:
            if line[0] == "false":
                continue
            else:
                print("Expected to be valid, found invalid, line {}".format(line_index))
                working = False
                break
    if working:
        print("The operation ended successfully!")


test()
