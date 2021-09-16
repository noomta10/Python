def main():
    txt = input("enter a sentence: ")
    splitting = txt.lower().split()
    order = sorted(splitting)
    for word in order:
        print(word)


main()
