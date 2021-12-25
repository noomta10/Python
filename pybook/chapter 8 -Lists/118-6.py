try:
    number_list = []
    number = ""
    while True:
        number = input("enter a number: ")
        if number == "done":
            break
        number_list.append(float(number))
    print("maximum {} minimum {}".format(max(number_list), min(number_list)))
except ValueError:
    print("it is not a number")
