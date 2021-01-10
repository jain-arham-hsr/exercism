class Garden:

    default_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    plant_names = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }

    def __init__(self, diagram, students=default_students):
        students = sorted(students)
        diagram = diagram.splitlines()
        first_row, second_row = diagram[0], diagram[1]
        self.all_plants = {}
        for i, student in zip(range(1, int(len(diagram[0])/2)+1), students):
            self.all_plants[student] = [self.plant_names[first_row[2*i-2]], self.plant_names[first_row[2*i-1]], self.plant_names[second_row[2*i-2]], self.plant_names[second_row[2*i-1]]]

    def plants(self, student_name):
        return self.all_plants[student_name]
