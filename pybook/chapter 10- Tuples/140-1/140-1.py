def main():
    file = open("mbox-short.txt", "r")
    mails_dictionary = {}
    for line in file:
        if line.startswith("From: "):
            line = line.split()
            mail = line[1]
            mail_counter(mail, mails_dictionary)
    dictionary_to_list(mails_dictionary)


def mail_counter(mail, mails_dictionary):
    if mail not in mails_dictionary:
        mails_dictionary[mail] = 1
    else:
        mails_dictionary[mail] += 1


def dictionary_to_list(mails_dictionary):
    mails_list = []
    for key, val in mails_dictionary.items():
        mails_list.append((val, key))
    mails_list.sort(reverse=True)
    for key, val in mails_list:
        print(val, key)
        break


main()
