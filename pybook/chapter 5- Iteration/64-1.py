try:
    num = ""
    total = 0
    count = 0
    while num != "done":
        num = input("enter a number: ")
        if num == "done":
            break
        total += int(num)
        count += 1
    print(total, count, total / count)
except ValueError:
    print("it is not a number")
