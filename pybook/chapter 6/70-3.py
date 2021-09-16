def count(string, required_letter):
    count_letter = 0
    for letter in string:
        if letter == required_letter:
            count_letter += 1
    print(count_letter)


count("banana", "a")
count("noam", "o")
