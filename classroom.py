from school import School

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []      # List of Student objects
        self.subjects = []      # List of Subject objects

    def add_student(self, student):
        roll_no = f"{self.name}-{len(self.students) + 1}"
        student.id = roll_no 
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()

    def get_top_students(self, top_n=3):
        # Sort students based on their overall grade and return the top N students
        sorted_students = sorted(self.students, key=lambda s: School.grade_to_value(s.grade), reverse=True)
        return sorted_students[:top_n]