def main():
    file_name = input('Enter the file name: ')
    try:
        file = open(file_name, "r")
    except:
        print('File cannot be opened:', file_name)
        exit()
    domain_names = dict()
    for line in file:
        if line.startswith("From: "):
            at_position = line.find("@")
            counter(line[at_position + 1:-1], domain_names)
    print(domain_names)


def counter(word, domain_names):
    if word not in domain_names:
        domain_names[word] = 1
    else:
        domain_names[word] += 1


main()
