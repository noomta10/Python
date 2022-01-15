import re


def main():
    formula = input("Enter formula: ")

    check_valid(formula)


def check_valid(formula):
    # number = "(-?[0-9]*(\\.[0-9]*)?)|(-?[a-zA-Z])"
    number = "(-?[0-9]*(\\.[0-9]*)?)([a-zA-Z])?"
    operator = "[-+*/]"
    correct_formula_pattern = "^({} {} )*{}$".format(number, operator, number)
    is_it_valid = re.findall(correct_formula_pattern, formula)
    if len(is_it_valid) == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
