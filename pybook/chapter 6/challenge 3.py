
def replace_once(line):
    duppos = line.find("duplicate")
    sppos = line.find(" ", duppos)
    num = int(line[sppos + 1])
    wordpos = line.find(" ", sppos + 1)
    wordend = line.find(" ", wordpos + 1)
    word = line[wordpos + 1:wordend]
    word = word + " "
    return line[:duppos] + word * num + line[wordend + 1:]


def main():
    sentence = input("write a sentence: ")
    while "duplicate" in sentence:
        sentence = replace_once(sentence)
    print(sentence)


main()
