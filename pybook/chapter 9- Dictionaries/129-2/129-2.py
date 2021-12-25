def main():
    file_name = input('Enter the file name: ')
    try:
        file = open(file_name, "r")
    except:
        print('File cannot be opened:', file_name)
        exit()
    counts = dict()
    for line in file:
        if line.startswith("From "):
            words = line.split()
            day = words[2]
            counter(day, counts)
    print(counts)


def counter(day, counts):
    if day not in counts:
        counts[day] = 1
    else:
        counts[day] += 1


main()
