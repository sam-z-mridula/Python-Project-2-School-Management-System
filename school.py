class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}      # {"subject": teacher_object}
        self.classrooms = {}    # {"classroom_name": classroom_object}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    
    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        # Logic to admit a student to the school
        pass

    @staticmethod
    def calculate_grade(marks):
        if marks <= 100 and marks >= 80:
            return 'A+'
        elif marks < 80 and marks >= 70:
            return 'A'
        elif marks < 70 and marks >= 60:
            return 'A-'
        elif marks < 60 and marks >= 50:
            return 'B'
        elif marks < 50 and marks >= 40:
            return 'C'
        elif marks < 40 and marks >= 33:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_mapping = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.00,
            'D': 1.00,
            'F': 0.00
        }
        return grade_mapping[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value == 5.00:
            return 'A+'
        elif value >= 4.00 and value < 5.00:
            return 'A'
        elif value >= 3.50 and value < 4.00:
            return 'A-'
        elif value >= 3.00 and value < 3.50:
            return 'B'
        elif value >= 2.00 and value < 3.00:
            return 'C'
        elif value >= 1.00 and value < 2.00:
            return 'D'
        else:
            return 'F'
        

    # def __repr__(self):
        # All Classrooms
        # All Teachers
        # All Students
        # All Subjects
        # All Student's results