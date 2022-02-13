from datetime import datetime


def main():
    file = open("salary.txt", "r")
    line_index = 1
    month_hours = {}
    month_extra = {}
    day_hour = {}
    for line in file:
        if line_index == 1:
            hour_pay = int(line)
        elif line_index == 2:
            normal_hours_count = int(line)
        elif line_index == 3:
            extra_add_percent = float(line)
        else:
            calculate_line_hours(line, day_hour)
        line_index += 1

    split_hours(day_hour, normal_hours_count, month_hours, month_extra)
    calculate_payment(hour_pay, extra_add_percent, month_hours, month_extra)


def calculate_line_hours(line, day_hour):
    line = line.split()

    date = line[0]
    start_time_string = line[1]
    end_time_string = line[2]

    time_format = "%Y_%m_%d %H:%M"
    start_time = datetime.strptime(date + " " + start_time_string, time_format)
    end_time = datetime.strptime(date + " " + end_time_string, time_format)

    total_hours = (end_time - start_time).total_seconds() / 3600
    day_hour[(start_time.month, start_time.day)] = total_hours


def split_hours(day_hour, normal_hours_count, month_hours, month_extra):
    for key, hours in day_hour.items():
        month = key[0]
        if hours <= normal_hours_count:

            if month not in month_hours:
                month_hours[month] = hours
            else:
                month_hours[month] += hours
        else:
            if month not in month_hours:
                month_hours[month] = normal_hours_count
            else:
                month_hours[month] += normal_hours_count

            extra_hours = hours - normal_hours_count
            if month not in month_extra:
                month_extra[month] = extra_hours
            else:
                month_extra[month] += extra_hours


def calculate_payment(hour_pay, extra_add_percent, month_hours, month_extra):
    file = open("calculation.txt", "w")
    for month in month_hours:
        if month not in month_extra:
            month_extra[month] = 0
        payment_normal = month_hours[month] * hour_pay
        payment_extra = month_extra[month] * (1 + extra_add_percent / 100) * hour_pay
        total_payment = payment_extra + payment_normal
        line = "Month: {}\n Hours normal: {}\n Hours extra: {}\n" \
               " payment normal: {}\n Payment extra: {}\n Payment total: {}\n\n"
        file.write(
            line.format(
                month, month_hours[month], month_extra[month],
                payment_normal, payment_extra, total_payment))


main()
