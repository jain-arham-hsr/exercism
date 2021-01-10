class School:
    def __init__(self):
        self.roster_dict = {}

    def add_student(self, name, grade):
        self.roster_dict.setdefault(grade, []).append(name)

    def roster(self):
        return [student for grade, students in sorted(self.roster_dict.items()) for student in sorted(students)]

    def grade(self, grade_number):
        return sorted(self.roster_dict.get(grade_number, []))
