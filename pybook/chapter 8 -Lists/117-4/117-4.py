def main():
    file = open("romeo.txt", "r")
    unique_words = []
    for line in file:
        words = line.lower().split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
            else:
                continue
    unique_words.sort()
    print(unique_words)

main()


