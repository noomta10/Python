file_name = input("Enter a file name: ")
try:
    file_name = open(file_name)
except:
    print("File can not be opened", file_name)
    exit()

spam_count = 0
total = 0
for line in file_name:
    if line.startswith("X-DSPAM-Confidence"):
        spam_count += 1
        colon_position = line.find(":")
        slash_position = line.find("\n")
        text = line[colon_position + 2: slash_position - 1]
        number = float(text)
        total += number

print("Average spam confidence: ", total / spam_count)

