def main():
    sentence = input("write a sentence: ")
    if "duplicate" in sentence:
        duppos = sentence.find("duplicate")
        print(sentence)
    else:
        print(sentence)

main()