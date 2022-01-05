import re


def main():
    formula = input("Enter formula: ")
    # number = "[-]?[0-9]+[.]+?"
    number = "[0-9]"
    operator = "[-+*/]"
    correct_formula_pattern = "^({} {} )*{}$".format(number, operator, number)
    check = re.findall(correct_formula_pattern, formula)

    if check == "None":
        print("The formula is NOT valid")
    else:
        print("The formula is valid")

def check_valid(formula):
    return True
#
# def test():
#     file = open("test.txt", "r")
#     number = "((-?[0-9]*(\\.[0-9]*)?)|([a-z]))"
#     operator = "[-+*/]"
#     correct_formula_pattern = "^({} {} )*{}$".format(number, operator, number)
#     for line in file:
#         line = line.rstrip()
#         is_it_valid = re.findall(correct_formula_pattern, line)
#         if len(is_it_valid) == 0:
#             print("The formula is NOT valid")
#         else:
#             print("The formula is valid {}".format(is_it_valid))

main()




(
    (
        -?
        [0-9]*
        (
            \\.
            [0-9]*
        )
        ?
    )
    |
    (
        [a-z]
    )
)