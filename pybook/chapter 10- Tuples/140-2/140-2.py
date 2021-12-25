def main():
    file = open("mbox-short.txt", "r")
    hours_counts = {}
    for line in file:
        if line.startswith("From "):
            pull_hour(line, hours_counts)
    dictionary_to_list(hours_counts)


def pull_hour(line, hours_counts):
    colon_position = line.find(":")
    hour = line[colon_position - 2:colon_position]
    if hour not in hours_counts:
        hours_counts[hour] = 1
    else:
        hours_counts[hour] += 1


def dictionary_to_list(hours_counts):
    hours_list = []
    for key, value in hours_counts.items():
        hours_list.append((key, value))
    hours_list.sort()
    for key, value in hours_list:
        print(key, value)


main()
