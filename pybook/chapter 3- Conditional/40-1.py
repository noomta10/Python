hours = float(input("enter hours: "))
rate = float(input("enter rate: "))
if hours > 40:
    print(40 * rate + (hours - 40) * 1.5 * rate)
else:
    print(hours * rate)