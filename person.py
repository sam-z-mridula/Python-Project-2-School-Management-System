import random
from school import School

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        # Logic for teaching
        pass

    def evaluate_exam(self):
        return random.randint(1, 100) # Simulating marks for the sake of example
    

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None  # Private attribute for student ID
        self.marks = {}   # {"subject": marks}
        self.subject_grade = {}  # {"subject": grade}
        self.grade = None  # Overall grade

    def calculate_final_grade(self):
        total_marks = 0
        for grade in self.subject_grade.values():
            total_marks += School.grade_to_value(grade)

        gpa = total_marks / len(self.subject_grade) # if self.subject_grade else 0
        self.grade = School.value_to_grade(gpa)

    @property
    def id(self):
        return self.__id        # Getter method for student ID
    
    @id.setter
    def id(self, value):
        self.__id = value       # Setter method for student ID