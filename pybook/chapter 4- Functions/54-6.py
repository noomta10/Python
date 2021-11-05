def compute_pay(hours, rate):
    if hours > 40:
        print(40 * rate + (hours - 40) * 1.5 * rate)
    else:
        print(hours * rate)


compute_pay(45, 10)
