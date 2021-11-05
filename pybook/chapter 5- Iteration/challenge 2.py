height = int(input("enter height: "))
for row in range(height):
    number = 1
    for spaces in range(height - row):
        print("", end=" ")
    for col_increase in range(row + 1):
        print(number, end=" ")
        number += 1
    print()

for row in range(height):
    number = 1
    print()
    for spaces in range(2*(height - row)):
        print("", end=" ")
    for col_increase in range(0, row + 1):
        print(number, end=" ")
        number += 1

    number -= 2

    for col_decrease in range(0, row):
        print(number, end=" ")
        number -= 1


print()
