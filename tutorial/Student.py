class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self. gpa = gpa

    def on_honor_rol(self):
        if self.gpa >= 95:
            return True
        else:
            return False