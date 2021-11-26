def main():
    file = open("input.txt", "r")
    unique_numbers = []
    for number in file:
        number = int(number.strip())
        if number not in unique_numbers:
            unique_numbers.append(number)
        else:
            continue
    unique_numbers.sort()
    for x in range(len(unique_numbers)):
        print(unique_numbers[x])

main()
