def main():
    file = open("input.txt", "r")
    unique_numbers = []
    for number in file:
        number = int(number.strip())
        if number not in unique_numbers:
            unique_numbers.append(number)
    unique_numbers.sort()
    # for index_in_number in range(len(unique_numbers)):
    #     print(unique_numbers[index_in_number])
    for number in unique_numbers:
        print(number)

main()
