def main():
    sentence = input("enter a sentence: ")
    backwards = sentence[::-1]
    if sentence == backwards:
        print("yes")
    else:
        print("no")


main()
