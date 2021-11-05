def parse(line):
    columns = []
    column = ""
    state = "first character"
    for character in line:
        if state == "first character":
            if character == '"':
                state = "quote col"
            else:
                state = "ordinary col"
                column = column + character
        elif state == "quote col":
            if character == '"':
                state = "wait for comma"
                columns.append(column)
                column = ""
            elif character == "\n":
                columns.append(column)
            else:
                column = column + character
        elif state == "wait for comma":
            if character == ",":
                state = "first character"
        elif state == "ordinary col":
            if character == ",":
                columns.append(column)
                column = ""
                state = "first character"
            elif character == "\n":
                columns.append(column)
            else:
                column = column + character
    return columns


def main():
    input_file = open("input.csv", "r")
    column_name = input("enter a column name: ")
    first_line = True
    for line in input_file:
        columns = parse(line)
        if first_line:
            header_index = columns.index(column_name)
            first_line = False
        else:
            print(columns[header_index])


main()
