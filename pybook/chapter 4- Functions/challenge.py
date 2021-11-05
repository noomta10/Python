import random


def run_casino(low, high, threshold):
    random_num = random.randint(low, high)
    if random_num > threshold:
        print("YOU WIN")
    else:
        print("YOU LOOSE")


def get_input():
    low = int(input("enter low number: "))
    high = int(input("enter high number: "))
    threshold = int(input("enter threshold: "))
    run_casino(low, high, threshold)
    run_casino(low, high, threshold)
    run_casino(low, high, threshold)


get_input()
