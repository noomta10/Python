import urllib.request

url = input("Enter URL: ")
file_handler = urllib.request.urlopen(url)
character_count = 0
character_printed = 0
for line in file_handler:
    character_count += len(line)
    if character_printed < 3000:
        if character_count < 3000:
            print(line.decode().strip())
            character_printed += len(line)
        else:
            print(line[0:3000-character_printed].decode().strip())
            character_printed = 3000
print("Total number of characters: {}.".format(character_count))
