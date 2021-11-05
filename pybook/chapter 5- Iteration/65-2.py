try:
    num = ""
    total = 0
    count = 0
    smallest = None
    largest = None
    while num != "done":
        num = input("enter a number: ")
        if num == "done":
            break
        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest:
            largest = num

        total += int(num)
        count += 1
    print(total, count, smallest, largest)
except ValueError:
    print("it is not a number")