input_file = open("input.txt")
output_file = open("output.txt", "w")

for line in input_file:
    if " ugly " in line:
        line = line.replace(" ugly ", "great")
    if line.startswith("ugly"):
        line = line.replace("ugly", "great")
    if line.endswith("ugly"):
        line = line.replace("ugly", "great")
    output_file.write(line)
