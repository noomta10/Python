def compute_grade(score):
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif 0.6 >= score >= 0:
        print("FAILED")

    else:
        print("bad score")


compute_grade(0.9)
