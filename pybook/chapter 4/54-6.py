def computepay(hours, rate):
  if hours > 40:
    print(40 * rate + (hours - 40) * 1.5 * rate)
  else:
    print(hours * rate)

#hours = float(input("enter hours: "))
#rate = float(input("enter rate: "))
computepay(45, 10)