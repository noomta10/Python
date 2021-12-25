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
            extra_add_percent = int(line)
        else:
            calculate_line_hours(line, day_hour)
        line_index += 1

    split_hours(day_hour, normal_hours_count, month_hours, month_extra)
    calculate_payment(hour_pay, extra_add_percent, month_hours, month_extra)


def calculate_line_hours(line, day_hour):
    line = line.split()
    date = line[0]
    month = date[5:7]
    day = date[8:10]

    start_time = line[1]
    start_hour_to_minutes = calculate_minutes(start_time)

    end_hour = line[2]
    end_hour_to_minutes = calculate_minutes(end_hour)

    total_minutes = end_hour_to_minutes - start_hour_to_minutes
    total_hours = total_minutes / 60
    day_hour[(month, day)] = total_hours


def calculate_minutes(time):
    time_split = time.split(sep=":")
    time_hour = time_split[0]
    time_minute = time_split[1]
    hour_to_min = int(time_hour) * 60 + int(time_minute)
    return hour_to_min


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
        file.write(
            "Month: {}\n Hours normal: {}\n Hours extra: {}\n" +
            " payment normal: {}\n Payment extra: {}\n Payment total: {}\n\n".format(
                month, month_hours[month], month_extra[month],
                payment_normal, payment_extra, total_payment))


main()
