line = ""
term = "blue"

while line != "quit":
    line = input("enter a line: ")
    if line == "quit":
        break
    if "blue" not in line:
        print(line)
