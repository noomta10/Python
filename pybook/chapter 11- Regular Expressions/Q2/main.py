import re


def main():
    formula = input("Enter formula: ")
    validation = check_valid(formula)
    if validation:
        print("The formula is valid")
    else:
        print("The formula is not valid")


def check_valid(formula):
    number = "(" \
             "(-?[0-9]+(\\.[0-9]*)?)([a-zA-Z])?" \
             "|" \
             "-?(\\.[0-9]+)([a-zA-Z])?" \
             "|" \
             "(-?[0-9]*(\\.[0-9]*)?)([a-zA-Z])" \
             ")"
    operator = "[-+*/]"
    correct_formula_pattern = '^({}\\s*{}\\s*)*{}$'.format(number, operator, number)
    matches = re.findall(correct_formula_pattern, formula)
    if len(matches) != 0:
        return True



if __name__ == "__main__":
    main()
