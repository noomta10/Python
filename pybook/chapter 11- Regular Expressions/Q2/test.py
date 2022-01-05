from main import check_valid

def test():
    file = open("test.txt", "r")
    for line in file:
        is_it_valid = check_valid(line)
        if len(is_it_valid) == 0:
            print("The formula is NOT valid")
        else:
            print("The formula is valid {}".format(is_it_valid))

test()
