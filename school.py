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
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)

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
        

    def __repr__(self):
        # All Classrooms
        print("-----ALL CLASSES-----")
        for key in self.classrooms.keys():
            print(f"{key}")
        print()

        # All Students
        print("-----ALL STUDENTS:-----")
        stu = ''
        for key, val in self.classrooms.items():
            stu += f"⭐ {key.upper()}:\n"
            for student in val.students:
                stu += f"{student.id}: {student.name}\n"
            stu += '\n'
        print(stu)

        # All Subjects
        print("-----ALL SUBJECTS:-----")
        sub = ''
        for key, val in self.classrooms.items():
            sub += f"⭐ {key.upper()}\n"
            for subject in val.subjects:
                sub += f"{subject.name}\n"
            sub += '\n'
        print(sub)

        # All Teachers
        print("-----ALL TEACHERS-----")
        teach = ''
        for key, val in self.teachers.items():
            teach += f"{key.name.upper()}: {val.name} \n"
        print(teach)

        # All Student's results
        print("-----STUDENT RESULT-----")
        for key, val in self.classrooms.items():
        #     for subj in val.subjects:
        #         subj.exam(val.students)

            for stud in val.students:
                print(f"  {stud.name}:")
                for s, m in stud.marks.items():
                    print(f"{s} \t {m} \t {stud.subject_grade[s]}")
                print('Final Grade:', stud.calculate_final_grade())
                print()

        return ''