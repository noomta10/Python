def main():
    my_tuple = (1, 2, 3, 4, 5)
    my_list = [1, 2, 3, 4, 5]
    updated_list = remove_from_list(my_list)
    print(updated_list)
    updated_tuple = remove_from_tuple(my_tuple)
    print(updated_tuple)


def remove_from_list(my_list):
    my_list.pop(1)
    return my_list


def remove_from_tuple(my_tuple):
    return my_tuple[0:1] + my_tuple[2:]


main()
