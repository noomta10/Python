input_file = open("input.txt")
for line in input_file:
    if line.startswith("name: "):
        colon_position = line.find(":")
        file_name = line[colon_position+2:-1]
        output_file = open(file_name, 'w')
    else:
        output_file.write(line)

