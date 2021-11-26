def middle(t):
    return t[1:-1]


def chop(t):
    t = t[1:-1]


t = [1, 2, 3, 4, 5, 6]
good_example = middle(t)
bad_example = chop(t)
print(good_example, bad_example)