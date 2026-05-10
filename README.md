# School Management System
This project implements a basic school management system in Python. It consists of classes representing a School, ClassRoom, Subject, Teacher, and Student.

## 1. School
1. Attributes:
    - name: Name of the school.
    - address: Address of the school.
    - teachers: Dictionary to store teachers associated with subjects.
    - classrooms: Dictionary to store classrooms.
2. Methods:
    - add_classroom(classroom): Adds a classroom to the school.
    - add_teacher(subject, teacher): Adds a teacher to a specific subject.
    - student_admission(student): Enrolls a student into a classroom.
    - calculate_grade(marks): Static method to calculate the grade based on marks.
    - grade_to_value(grade): Static method to convert grade to its corresponding value.
    - value_to_grade(value): Static method to convert value to its corresponding grade.
    - __repr__(): String representation of the school, including classroom details and student exam marks.

## 2. ClassRoom
1. Attributes:
    - name: Name of the classroom.
    - students: List to store students.
    - subjects: List to store subjects taught in the classroom.
2. Methods:
    - add_student(student): Adds a student to the classroom.
    - add_subject(subject): Adds a subject to the classroom.
    - take_semester_final(): Conducts semester final exams for all subjects.
    - get_top_students(): Method to sort students by grade (TODO).

## 3. Subject
1. Attributes:
    - name: Name of the subject.
    - teacher: Teacher associated with the subject.
    - max_marks: Maximum marks for the subject.
    - pass_marks: Passing marks for the subject.
2. Methods:
    - exam(students): Conducts exam for students and records their marks.

## 4. Person
1. Attributes:
    - name: Name of the person.

## 5. Teacher (inherits from Person)
1. Attributes:
    - Inherits name from Person.
2. Methods:
    - teach(): Placeholder method for teaching.
    - evaluate_exam(): Evaluates exams and returns random marks.

## 6. Student (inherits from Person)
1. Attributes:
    - Inherits name from Person.
    - classroom: Classroom the student is enrolled in.
    - marks: Dictionary to store marks obtained in subjects.
    - subject_grade: Dictionary to store grades obtained in subjects.
    - grade: Final grade of the student.
2. Methods:
    - calculate_final_grade(): Calculates the final grade of the student.
3. Properties:
    - id: Getter and setter for student ID.



