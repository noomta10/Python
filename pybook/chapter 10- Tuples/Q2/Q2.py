def main():
    file = open("input.txt", "r")
    name_age_to_height = {}
    for line in file:
        parse_line(line, name_age_to_height)
    while True:
        get_user_input(name_age_to_height)
        answer = input("Do you have another query (yes/no): ")
        if answer == "no":
            break


def parse_line(line, name_age_to_height):
    line = line.split()
    first_name = line[0]
    last_name = line[1]
    age = line[2]
    height = line[3]
    my_tuple = (first_name, last_name, age)
    name_age_to_height[my_tuple] = height


def get_user_input(name_age_to_height):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = input("Enter age: ")
    user_input = (first_name, last_name, age)
    if user_input in name_age_to_height:
        print("The height is: " + name_age_to_height[user_input])
    else:
        print("Sorry, not found")


main()
