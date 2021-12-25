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
    print(mails)


def counter(mail, mails):
    if mail not in mails:
        mails[mail] = 1
    else:
        mails[mail] += 1


main()
