file = open("words.txt", "r")
dictionary = dict()
for line in file:
    words = line.split()
    for word in words:
        dictionary[word] = ""

print("noam" in dictionary)