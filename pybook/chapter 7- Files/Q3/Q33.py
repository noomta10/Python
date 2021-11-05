def parse(line):
    columns =[]
    col = ""
    state = "first character"
    for character in line:
        if state == "first character":
            if character == '"':
                state = "quote col"
            else:
                state = "ordinary col"
                col = col + character
        elif state == "quote col":
            if character == '"':
                state = "wait for comma"
                columns.append(col)
                col = ""
            elif character == "\n":
                columns.append(col)
            else:
                col = col + character
        elif state == "wait for comma":
            if character == ",":
                state = "first character"
        elif state == "ordinary col":
            if character == ",":
                columns.append(col)
                col = ""
                state = "first character"
            elif character == "\n":
                columns.append(col)
            else:
                col = col + character
    return columns



def main():
    input_file = open("input.csv", "r")
    column_name = input("enter a column name: ")
    col_count = 1
    for line in input_file:
        columns = parse(line)
        if col_count == 1:
            index = int(columns.index(column_name))
            col_count += 1
        else:
            print(columns[index])

main()


