def main():
    sentence = input("write a sentence: ")
    if "duplicate" in sentence:
        duppos = sentence.find("duplicate")
        sppos = sentence.find(" ", duppos)
        num = int(sentence[sppos+1])
        wordpos = sentence.find(" ", sppos+1)
        wordend = sentence.find(" ", wordpos+1)
        word = sentence[wordpos:wordend]
        print(sentence[:duppos] + word * num + sentence[wordend:])

    else:
        print(sentence)


main()
