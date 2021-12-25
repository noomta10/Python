def main():
    file_name = input('Enter the file name: ')
    try:
        file = open(file_name, "r")
    except:
        print('File cannot be opened:', file_name)
        exit()
    mails = dict()
    for line in file:
        if line.startswith("From "):
            words = line.split()
            counter(words[1], mails)
    find_max(mails)


def counter(mail, mails):
    if mail not in mails:
        mails[mail] = 1
    else:
        mails[mail] += 1


def find_max(mails):
    largest = None
    numbers = list(mails.values())
    for number in numbers:
        if largest is None or number > largest:
            largest = number
    for key in mails:
        if mails[key] == largest:
            print(key, mails[key])


main()
